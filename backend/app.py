from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
import subprocess
import json
import os
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        project_root = os.path.abspath("..")

        build_script = os.path.join(project_root, "scripts/build.sh")

        subprocess.run(["chmod", "+x", build_script])

        result = subprocess.run(
            [build_script],
            cwd=project_root,
            capture_output=True,
            text=True
        )

        print("\n=== C++ BUILD OUTPUT ===")
        print(result.stdout)

        if result.stderr:
            print("\n=== BUILD ERRORS ===")
            print(result.stderr)

    except Exception as e:
        print("Build failed:", str(e))

    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return FileResponse("static/index.html")

@app.get("/api/stats")
def get_stats():
    try:
        binary_path = os.path.abspath("../bin/system_monitor")

        result = subprocess.run(
            [binary_path],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return {"error": "Empty output", "stderr": result.stderr}

        return json.loads(output)

    except Exception as e:
        return {"error": str(e)}

@app.get("/api/scheduler")
def get_scheduler():
    try:
        binary_path = os.path.abspath("../bin/fcfs")

        result = subprocess.run(
            [binary_path],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if not output:
            return {"error": "Empty output", "stderr": result.stderr}

        return json.loads(output)

    except Exception as e:
        return {"error": str(e)}
    
@app.post("/api/scheduler")
async def run_scheduler(request: Request):
    try:
        processes = await request.json()

        binary_path = os.path.abspath("../bin/fcfs")

        # Convert input to string format for CLI
        input_data = json.dumps(processes)
        
        result = subprocess.run(
            [binary_path],
            input=input_data,
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        print(f"Scheduler input: {input_data}")
        print(f"Scheduler output: {output}")
        if not output:
            return {"error": "Empty output", "stderr": result.stderr}

        return json.loads(output)

    except Exception as e:
        return {"error": str(e)}