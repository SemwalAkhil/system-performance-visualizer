# System Performance Visualizer & CPU Scheduler Simulator

<p align="center">

A cloud-enabled system monitoring and operating system visualization project built with a C++ system engine and FastAPI backend.

</p>

<p align="center">

![C++](https://img.shields.io/badge/C%2B%2B-System%20Engine-blue)
![Python](https://img.shields.io/badge/Python-FastAPI-green)
![Linux](https://img.shields.io/badge/Linux-%2Fproc%20filesystem-orange)
![API](https://img.shields.io/badge/API-REST-lightgrey)
![Deployment](https://img.shields.io/badge/Deployment-AWS%20EC2-blueviolet)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

</p>

---

## Description

A cloud-enabled system performance visualization and CPU scheduling simulation project developed using C++ for the system engine and Python (FastAPI) for the web backend.

The system demonstrates operating system concepts such as **CPU scheduling (FCFS)** and **system resource monitoring** through an interactive web-based interface.

It reads real-time performance statistics from the Linux `/proc` filesystem and exposes them through a REST API for visualization.

---

## Features

- CPU Scheduling Simulation (**FCFS**)
- Real-time CPU and Memory Monitoring
- REST API for system statistics
- Web-based dashboard visualization
- Controlled CPU load generation
- Cloud deployment on Linux (AWS EC2)

---

## Technologies Used

- C++ (system monitoring engine)
- Python (FastAPI backend)
- Uvicorn (ASGI server)
- Linux (`/proc` filesystem)
- HTML / CSS / JavaScript (Frontend Dashboard)
- Chart.js (data visualization)

---

## Deployment

The application is deployed on a Linux cloud virtual machine (AWS EC2).

It can be accessed through a web browser using the public IP address.

---

## API Endpoints

- `GET /api/stats` → Fetch CPU and memory usage  
- `POST /api/scheduler` → Run FCFS scheduling simulation  
- `POST /api/load/start` → Start CPU load  
- `POST /api/load/stop` → Stop CPU load  

---

## Development Environment

The project uses a portable development environment based on **GitHub Codespaces** and **Dev Containers**.

This allows the project to be developed from any computer without installing local dependencies.

---

## Running the Backend

```bash
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000
````

Access API:

```
/api/stats
```

---

## Repository Structure

```
system-performance-visualizer
│
├── src/                # C++ system monitoring engine
├── backend/            # FastAPI backend service
├── frontend/           # Web dashboard (if present)
├── docs/               # Project documentation
├── scripts/            # Build scripts
├── .devcontainer/      # Dev container configuration
└── README.md
```

---

## System Design Diagrams

Includes:

* System Architecture
* Sequence Diagram
* Data Flow Diagrams (Level 0 & 1)
* GUI Design

(Already linked in docs)

---

## Project Roadmap

| Phase    | Description                  | Status        |
| -------- | ---------------------------- | ------------- |
| Phase 1  | Setup & Repository Structure | ✅ Completed   |
| Phase 2  | C++ Monitoring Engine        | ✅ Completed   |
| Phase 3  | Architecture Design          | ✅ Completed   |
| Phase 4  | FastAPI Backend              | ✅ Completed   |
| Phase 5  | Frontend Dashboard           | ✅ Completed   |
| Phase 6  | Scheduling (FCFS)            | ✅ Completed   |
| Phase 7  | Load Generation              | ✅ Completed   |
| Phase 8  | UI Integration               | ✅ Completed   |
| Phase 9  | Cloud Deployment             | ✅ Completed   |
| Phase 10 | Testing & Validation         | ✅ Completed   |
| Phase 11 | Final Documentation          | 🔄 In Progress |

---

## Academic Context

Developed as a Major Project for the Bachelor of Computer Applications (BCA) program.

---

## Viva Preparation

* [Viva Notes](docs/viva/README.md)

---

## Development Notes

* [Development Rules](docs/development/README.md)

---

## Project Plan

* [Plan of Action](docs/plan/planOfAction.md)

---

## Status

✅ Completed and Deployed
