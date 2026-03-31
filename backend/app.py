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

PROJECT_ROOT = os.getcwd()

# Handle both local + cloud structures
STATIC_DIR = os.path.join(PROJECT_ROOT, "static")
if not os.path.exists(STATIC_DIR):
    STATIC_DIR = os.path.join(PROJECT_ROOT, "backend", "static")

BIN_DIR = os.path.join(PROJECT_ROOT, "bin")
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, "scripts")

SYSTEM_MONITOR_BIN = os.path.join(BIN_DIR, "system_monitor")
FCFS_BIN = os.path.join(BIN_DIR, "fcfs")
BUILD_SCRIPT = os.path.join(SCRIPTS_DIR, "build.sh")

CPU_STEP = max(1, (os.cpu_count() or 1) // 4)

# 🔥 Dynamic memory block size based on total RAM (safer limits)
try:
    import psutil
    TOTAL_RAM = psutil.virtual_memory().total

    # smaller chunks (~0.2% RAM instead of 1%)
    MEM_BLOCK_SIZE = max(1 * 1024 * 1024, TOTAL_RAM // 500)

    # cap total memory usage to 30% of system RAM
    MAX_MEMORY_USAGE = TOTAL_RAM * 0.3
except Exception:
    MEM_BLOCK_SIZE = 2 * 1024 * 1024  # fallback (2MB)
    MAX_MEMORY_USAGE = 200 * 1024 * 1024  # 200MB cap

MEM_STEP = 2

# =====================================================
# GLOBAL STATE
# =====================================================

execution_thread: threading.Thread | None = None
is_running: bool = False
current_process: int | None = None
execution_done: bool = False

cpu_processes: List[subprocess.Popen] = []
memory_blocks: List[bytearray] = []

# =====================================================
# UTILITIES
# =====================================================

def run_binary(path: str, input_data: str | None = None) -> Dict[str, Any]:
    try:
        if os.path.exists(path):
            os.chmod(path, 0o755)
    except Exception:
        pass

    try:
        result = subprocess.run(
            [path],
            input=input_data,
            capture_output=True,
            text=True
        )

        output = (result.stdout or "").strip()

        if not output:
            return {"error": "Empty output", "stderr": result.stderr}

        return json.loads(output)

    except Exception as e:
        return {"error": str(e)}

# =====================================================
# LIFESPAN
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("=== PATH DEBUG ===")
        print("PROJECT_ROOT:", PROJECT_ROOT)
        print("STATIC_DIR:", STATIC_DIR)
        print("BIN_DIR:", BIN_DIR)

        if os.path.exists(BUILD_SCRIPT):
            subprocess.run(["chmod", "+x", BUILD_SCRIPT])
            try:
                result = subprocess.run([BUILD_SCRIPT], cwd=PROJECT_ROOT, capture_output=True, text=True)
                print("=== BUILD OUTPUT ===")
                print(result.stdout)
                if result.stderr:
                    print(result.stderr)
            except Exception:
                print("Build failed, using existing binaries")
        else:
            print("Build script not found, skipping")

    except Exception as e:
        print("Startup error:", str(e))

    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# =====================================================
# ROUTES
# =====================================================

@app.get("/")
def home():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


@app.get("/api/stats")
def get_stats():
    try:
        data = run_binary(SYSTEM_MONITOR_BIN)
        if "error" in data:
            raise Exception()
        return data
    except Exception:
        try:
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


@app.get("/api/current")
def get_current_process():
    return {"current": current_process, "done": execution_done}

# =====================================================
# EXECUTION ENGINE
# =====================================================

def execute_processes(processes: List[Dict[str, Any]]):
    global is_running, current_process, execution_done

    is_running = True
    execution_done = False

    processes_sorted = sorted(processes, key=lambda p: p.get("arrival", 0))
    current_time = 0

    for p in processes_sorted:
        if not is_running:
            break

        arrival = int(p.get("arrival", 0))
        burst = max(1, int(p.get("burst", 1)))

        if current_time < arrival:
            current_process = None
            time.sleep(arrival - current_time)
            current_time = arrival

        current_process = int(p.get("id"))

        cpu_add()
        memory_add()

        time.sleep(burst)
        current_time += burst

        cpu_reduce()
        memory_reduce()

    current_process = None
    is_running = False
    execution_done = True


def start_execution(processes: List[Dict[str, Any]]):
    global execution_thread
    stop_execution()

    execution_thread = threading.Thread(
        target=execute_processes,
        args=(processes,),
        daemon=True
    )
    execution_thread.start()


def stop_execution():
    global is_running, current_process
    is_running = False
    current_process = None

# =====================================================
# SCHEDULER
# =====================================================

@app.post("/api/scheduler")
async def run_scheduler(request: Request):
    global is_running

    try:
        processes = await request.json()

        if not isinstance(processes, list):
            return {"error": "Invalid input"}

        if is_running:
            return {"error": "Execution already running"}

        data = run_binary(FCFS_BIN, json.dumps(processes))

        if "error" in data:
            processes_sorted = sorted(processes, key=lambda p: p["arrival"])

            current_time = 0
            result = []
            timeline = []

            for p in processes_sorted:
                arrival = int(p["arrival"])
                burst = int(p["burst"])

                if current_time < arrival:
                    current_time = arrival

                start = current_time
                completion = start + burst
                turnaround = completion - arrival
                waiting = turnaround - burst

                result.append({
                    "id": p["id"],
                    "arrival": arrival,
                    "burst": burst,
                    "start": start,
                    "completion": completion,
                    "waiting": waiting,
                    "turnaround": turnaround
                })

                for _ in range(start, completion):
                    timeline.append(p["id"])

                current_time = completion

            data = {"processes": result, "timeline": timeline, "fallback": True}

        start_execution(processes)
        return data

    except Exception as e:
        return {"error": str(e)}

# =====================================================
# LOAD CONTROL
# =====================================================

@app.post("/api/load/cpu/add")
def cpu_add():
    global cpu_processes
    for _ in range(CPU_STEP):
        p = subprocess.Popen(["yes"], stdout=subprocess.DEVNULL)
        cpu_processes.append(p)
    return {"status": "CPU load increased", "running_processes": len(cpu_processes)}


@app.post("/api/load/cpu/reduce")
def cpu_reduce():
    global cpu_processes
    for _ in range(min(CPU_STEP, len(cpu_processes))):
        p = cpu_processes.pop()
        p.terminate()
        p.wait()
    return {"status": "CPU load reduced", "running_processes": len(cpu_processes)}


@app.post("/api/load/cpu/stop")
def cpu_stop():
    global cpu_processes
    for p in cpu_processes:
        p.terminate()
        p.wait()
    cpu_processes.clear()
    return {"status": "CPU load stopped"}


@app.post("/api/load/memory/add")
def memory_add():
    global memory_blocks

    current_usage = len(memory_blocks) * MEM_BLOCK_SIZE

    # 🔥 Prevent excessive memory usage
    if current_usage >= MAX_MEMORY_USAGE:
        return {
            "status": "Memory limit reached",
            "current_mb": current_usage // (1024 * 1024)
        }

    for _ in range(MEM_STEP):
        if (len(memory_blocks) * MEM_BLOCK_SIZE) >= MAX_MEMORY_USAGE:
            break
        memory_blocks.append(bytearray(MEM_BLOCK_SIZE))

    return {
        "status": "Memory load increased",
        "block_size_mb": MEM_BLOCK_SIZE // (1024 * 1024),
        "total_blocks": len(memory_blocks)
    }


@app.post("/api/load/memory/reduce")
def memory_reduce():
    global memory_blocks
    for _ in range(min(MEM_STEP, len(memory_blocks))):
        memory_blocks.pop()
    return {"status": "Memory load reduced"}


@app.post("/api/load/memory/stop")
def memory_stop():
    global memory_blocks
    memory_blocks.clear()
    return {"status": "Memory load stopped"}

# =====================================================
# ENTRY
# =====================================================

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
