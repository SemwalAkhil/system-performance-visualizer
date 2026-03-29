from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import subprocess
import json
import os
import threading
import time
from typing import List, Dict, Any

# =====================================================
# CONFIG
# =====================================================

# Railway / cloud runs app from /app, so use current directory
# In deployment, backend folder itself is root (/app)
PROJECT_ROOT = os.getcwd()
BIN_DIR = os.path.join(PROJECT_ROOT, "bin")
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")

SYSTEM_MONITOR_BIN = os.path.join(BIN_DIR, "system_monitor")
FCFS_BIN = os.path.join(BIN_DIR, "fcfs")
BUILD_SCRIPT = os.path.join(SCRIPTS_DIR, "build.sh")

# Load tuning
CPU_STEP = max(1, (os.cpu_count() or 1) // 4)
MEM_BLOCK_SIZE = 10 * 1024 * 1024  # 10 MB
MEM_STEP = 5

# =====================================================
# GLOBAL STATE
# =====================================================

execution_thread: threading.Thread | None = None
is_running: bool = False
current_process: int | None = None  # currently executing process id
execution_done: bool = False  # 🔥 NEW FLAG

cpu_processes: List[subprocess.Popen] = []
memory_blocks: List[bytearray] = []

# =====================================================
# UTILITIES
# =====================================================

def run_binary(path: str, input_data: str | None = None) -> Dict[str, Any]:
    # Ensure binary is executable (important for cloud deployments)
    try:
        if os.path.exists(path):
            os.chmod(path, 0o755)
    except Exception:
        pass

    """Run a compiled C++ binary and return parsed JSON output."""
    result = subprocess.run(
        [path],
        input=input_data,
        capture_output=True,
        text=True
    )

    output = (result.stdout or "").strip()

    if not output:
        return {"error": "Empty output", "stderr": result.stderr}

    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON from binary", "raw": output}


# =====================================================
# APP LIFESPAN (BUILD C++ ON START)
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # ===== DEBUG PATHS =====
        print("=== PATH DEBUG ===")
        print("CWD:", os.getcwd())
        print("PROJECT_ROOT:", PROJECT_ROOT)
        print("SCRIPTS_DIR:", SCRIPTS_DIR)
        print("BUILD_SCRIPT:", BUILD_SCRIPT)

        # ===== DIRECTORY CHECK (ONLY IMPORTANT PATHS) =====
        print("=== IMPORTANT PATH DEBUG ===")

        important_paths = {
            "PROJECT_ROOT": PROJECT_ROOT,
            "BIN_DIR": BIN_DIR,
            "SCRIPTS_DIR": SCRIPTS_DIR,
            "BUILD_SCRIPT": BUILD_SCRIPT,
            "SYSTEM_MONITOR_BIN": SYSTEM_MONITOR_BIN,
            "FCFS_BIN": FCFS_BIN
        }

        for name, path in important_paths.items():
            exists = os.path.exists(path)
            print(f"{name}: {path} | EXISTS: {exists}")

        # ===== BUILD STEP =====
        # Cloud environments often DON'T have g++ installed
        # So we attempt build, but fail gracefully and rely on precompiled binaries
        if os.path.exists(BUILD_SCRIPT):
            subprocess.run(["chmod", "+x", BUILD_SCRIPT])

            try:
                result = subprocess.run(
                    [BUILD_SCRIPT],
                    cwd=PROJECT_ROOT,
                    capture_output=True,
                    text=True
                )

                print("=== C++ BUILD OUTPUT ===")
                print(result.stdout)

                if result.stderr:
                    print("=== BUILD ERRORS ===")
                    print(result.stderr)

                # If build failed, warn but continue
                if "g++" in (result.stderr or ""):
                    print("⚠ g++ not available — using precompiled binaries")

            except Exception as e:
                print("⚠ Build step failed, using existing binaries:", str(e))
        else:
            print(f"Build script not found at {BUILD_SCRIPT}, skipping build step.")

    except Exception as e:
        print("Build failed:", str(e))

    yield


app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# =====================================================
# ROUTES
# =====================================================

@app.get("/")
def home():
    return FileResponse("backend/static/index.html")


@app.get("/api/stats")
def get_stats():
    """Return CPU and memory usage.
    Falls back to Python-based stats if C++ binary fails (cloud compatibility).
    """
    try:
        data = run_binary(SYSTEM_MONITOR_BIN)

        # If binary failed due to GLIBC or runtime issue → fallback
        if "error" in data:
            raise Exception(data.get("stderr", "Binary failed"))

        return data

    except Exception:
        # 🔥 FALLBACK (NO C++ DEPENDENCY)
        try:
            import os
            import psutil

            cpu = psutil.cpu_percent(interval=0.5)
            memory = psutil.virtual_memory()

            return {
                "cpu": cpu,
                "memory": memory.used // (1024 * 1024),
                "total_memory": memory.total // (1024 * 1024),
                "fallback": True
            }
        except Exception as e:
            return {"error": str(e)}
    """Return CPU and memory usage from system_monitor binary."""
    try:
        return run_binary(SYSTEM_MONITOR_BIN)
    except Exception as e:
        return {"error": str(e)}


@app.get("/api/current")
def get_current_process():
    """Return currently executing process id and execution status."""
    return {
        "current": current_process,
        "done": execution_done
    }


# =====================================================
# SCHEDULER EXECUTION ENGINE (REAL-TIME LOAD)
# =====================================================


def execute_processes(processes: List[Dict[str, Any]]):
    """
    Execute processes using FCFS order (sorted by arrival time).
    Simulates CPU + memory load and updates current_process for UI sync.
    """
    global is_running, current_process, execution_done

    is_running = True
    execution_done = False

    # Ensure FCFS order
    processes_sorted = sorted(processes, key=lambda p: p.get("arrival", 0))

    current_time = 0

    for p in processes_sorted:
        if not is_running:
            break

        arrival = int(p.get("arrival", 0))
        burst = max(1, int(p.get("burst", 1)))

        # If CPU is idle, wait until next arrival
        if current_time < arrival:
            idle_time = arrival - current_time
            current_process = None  # mark idle
            time.sleep(idle_time)
            current_time = arrival

        # Mark running process
        current_process = int(p.get("id"))

        cpu_add()
        memory_add()

        # Execute
        time.sleep(burst)
        current_time += burst

        cpu_reduce()
        memory_reduce()

    # Reset after execution
    current_process = None
    is_running = False
    execution_done = True



def start_execution(processes: List[Dict[str, Any]]):
    """Start execution in a background thread (daemon)."""
    global execution_thread

    stop_execution()

    execution_thread = threading.Thread(
        target=execute_processes,
        args=(processes,),
        daemon=True
    )
    execution_thread.start()



def stop_execution():
    """Stop current execution safely."""
    global is_running, current_process

    is_running = False
    current_process = None


# =====================================================
# SCHEDULER API
# =====================================================

@app.post("/api/scheduler")
async def run_scheduler(request: Request):
    """
    1) Calls FCFS C++ binary to compute metrics
    2) Starts real-time execution simulation
    """
    global is_running

    try:
        processes = await request.json()

        # 🔥 BACKEND VALIDATION
        if not isinstance(processes, list):
            return {"error": "Invalid input format"}

        for p in processes:
            if not all(k in p for k in ("id", "arrival", "burst")):
                return {"error": "Invalid process structure"}

        # 🔥 PREVENT MULTIPLE EXECUTIONS
        if is_running:
            return {"error": "Execution already running"}

        data = run_binary(FCFS_BIN, json.dumps(processes))

        # 🔥 FALLBACK if C++ binary fails (GLIBC issue on cloud)
        if "error" in data:
            try:
                # Minimal FCFS fallback (Python)
                processes_sorted = sorted(processes, key=lambda p: p["arrival"])

                current_time = 0
                result = []

                for p in processes_sorted:
                    arrival = p["arrival"]
                    burst = p["burst"]

                    if current_time < arrival:
                        current_time = arrival

                    start = current_time
                    end = start + burst

                    result.append({
                        "id": p["id"],
                        "start": start,
                        "end": end
                    })

                    current_time = end

                data = {
                    "schedule": result,
                    "fallback": True
                }

            except Exception as e:
                return {"error": str(e)}

        # Start execution AFTER computing schedule
        start_execution(processes)

        return data

    except Exception as e:
        return {"error": str(e)}


# =====================================================
# CPU LOAD CONTROL (INCREMENTAL)
# =====================================================

@app.post("/api/load/cpu/add")
def cpu_add():
    """Increase CPU load by spawning 'yes' processes."""
    global cpu_processes
    try:
        for _ in range(CPU_STEP):
            p = subprocess.Popen(["yes"], stdout=subprocess.DEVNULL)
            cpu_processes.append(p)
        return {"status": "CPU load increased", "running_processes": len(cpu_processes)}
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/load/cpu/reduce")
def cpu_reduce():
    """Reduce CPU load by terminating some processes."""
    global cpu_processes
    try:
        to_kill = min(CPU_STEP, len(cpu_processes))
        for _ in range(to_kill):
            p = cpu_processes.pop()
            p.terminate()
            p.wait()  # 🔥 prevent zombie process
        return {"status": "CPU load reduced", "running_processes": len(cpu_processes)}
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/load/cpu/stop")
def cpu_stop():
    """Stop all CPU load processes."""
    global cpu_processes
    try:
        for p in cpu_processes:
            p.terminate()
            p.wait()  # 🔥 prevent zombie process
        cpu_processes.clear()
        return {"status": "CPU load stopped"}
    except Exception as e:
        return {"error": str(e)}


# =====================================================
# MEMORY LOAD CONTROL (INCREMENTAL)
# =====================================================

@app.post("/api/load/memory/add")
def memory_add():
    """Increase memory usage by allocating byte arrays."""
    global memory_blocks
    try:
        for _ in range(MEM_STEP):
            memory_blocks.append(bytearray(MEM_BLOCK_SIZE))
        return {"status": "Memory load increased"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/load/memory/reduce")
def memory_reduce():
    """Reduce memory usage by freeing allocated blocks."""
    global memory_blocks
    try:
        for _ in range(min(MEM_STEP, len(memory_blocks))):
            memory_blocks.pop()
        return {"status": "Memory load reduced"}
    except Exception as e:
        return {"error": str(e)}


@app.post("/api/load/memory/stop")
def memory_stop():
    """Free all allocated memory blocks."""
    global memory_blocks
    try:
        memory_blocks.clear()
        return {"status": "Memory load stopped"}
    except Exception as e:
        return {"error": str(e)}

# =====================================================
# ENTRY POINT (FOR CLOUD DEPLOYMENT)
# =====================================================

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)

