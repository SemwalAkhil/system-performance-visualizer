# Backend Service (FastAPI)

This directory contains the FastAPI backend responsible for exposing
system performance data and scheduling functionality via REST APIs.

---

## Overview

The backend acts as a bridge between:

- Frontend dashboard
- C++ system monitoring engine

It executes the compiled C++ binaries and returns structured JSON responses.

---

## API Endpoints

- `GET /api/stats`  
  Returns CPU and memory usage

- `POST /api/scheduler`  
  Executes FCFS scheduling simulation

- `POST /api/load/start`  
  Starts CPU load generation

- `POST /api/load/stop`  
  Stops CPU load generation

---

## How It Works

1. API request is received
2. Backend executes C++ binary using subprocess
3. Output is parsed into JSON
4. Response is sent to frontend

---

## Running the Backend

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
````

---

## Notes

* Backend is stateless
* No database is used
* All data is retrieved in real-time from the system
