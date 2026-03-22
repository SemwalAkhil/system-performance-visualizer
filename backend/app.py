from fastapi import FastAPI
from fastapi.responses import FileResponse
import subprocess
import json
import os

app = FastAPI()

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