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

<details>
<summary><strong>System Architecture Diagram</strong></summary>

<br>

The architecture diagram provides a high-level overview of the layered structure of the application.  
It shows how the **web client communicates with the FastAPI backend**, which then interacts with the **C++ monitoring engine** to retrieve system statistics from the Linux `/proc` filesystem.

Full source: [View Diagram Source](docs/diagrams/System_Architecture.md)

<p align="center">
<img src="docs/diagrams/System_Architecture.png" width="750">
</p>

</details>


<details>
<summary><strong>Sequence Diagram</strong></summary>
<br>

The sequence diagram illustrates the **runtime interaction between system components** when a user requests system statistics from the dashboard.

It shows how the browser sends a request to the backend API, the backend executes the monitoring engine, and the engine retrieves system metrics from the Linux kernel.

Full source: [View Diagram Source](docs/diagrams/Sequence_Diagram.md)

<p align="center">
<img src="docs/diagrams/Sequence_Diagram.png" width="750">
</p>

</details>

<details>
<summary><strong>Data Flow Diagram (Level 0)</strong></summary>

<br>

The Level 0 Data Flow Diagram (DFD) represents the **entire system as a single process** interacting with external entities such as the user and the Linux kernel.

Full source: [View Diagram Source](docs/diagrams/Data_Flow_Diagram_Level_0.md)

<p align="center">
<img src="docs/diagrams/Data_Flow_Diagram_Level_0.png" width="700">
</p>

</details>

<details>
<summary><strong>Data Flow Diagram (Level 1)</strong></summary>

<br>

The Level 1 DFD expands the system into internal components such as the browser, backend API, monitoring engine, and kernel data source.

This diagram explains how **data flows through the system during a monitoring request**.

Full source: [View Diagram Source](docs/diagrams/Data_Flow_Diagram_Level_1.md)

<p align="center">
<img src="docs/diagrams/Data_Flow_Diagram_Level_1.png" width="750">
</p>

</details>

<details>
<summary><strong>GUI Design Diagram</strong></summary>

<br>

The GUI design diagram represents the planned layout of the web dashboard interface used to visualize system performance statistics.

It illustrates how CPU usage charts, memory statistics, and system controls will be arranged in the user interface.

<p align="center">
<img src="docs/diagrams/Design_Diagram.png" width="750">
</p>

</details>

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
