# System Performance Visualizer & CPU Scheduler Simulator

## Description

A cloud-enabled system performance visualization and CPU scheduling simulation project developed using C++ for the system engine and Python (FastAPI) for the web backend. The project is designed to demonstrate operating system concepts such as CPU scheduling and system resource monitoring through an accessible web-based interface.

The system reads real-time performance statistics from the Linux `/proc` filesystem and exposes them through a REST API for visualization.

## Features

* CPU scheduling simulation (FCFS, SJF, Priority, Round Robin)
* Memory allocation visualization
* Real-time system performance monitoring
* REST API for system statistics
* Modular system monitoring engine written in C++

## Technologies Used

* C++ (system monitoring engine)
* Python (FastAPI backend)
* Uvicorn (ASGI server)
* Linux (`/proc` filesystem)
* HTML / CSS / JavaScript (planned frontend)

## Development Environment

The project uses a portable development environment based on **GitHub Codespaces** and **Dev Containers**.

This allows the project to be developed from any computer without installing local dependencies.

The dev container automatically installs:

* C++ build tools (g++)
* Python
* FastAPI dependencies
* Required VS Code extensions

When a Codespace starts, the environment is automatically prepared and the C++ monitoring engine is built using the project build script.

This ensures consistent development environments across multiple systems.

## Using GitHub Codespaces

The project can be developed directly in the browser using GitHub Codespaces.

### Steps

1. Open the repository on GitHub.
2. Click **Code**.
3. Select the **Codespaces** tab.
4. Click **Create Codespace on development**.

GitHub will automatically build the development container and install all dependencies.

Once the environment starts, the system monitor binary is built automatically.

### Running the Backend

```
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API endpoint can be accessed at:

```
/api/stats
```

## Repository Structure

The project follows a structured repository layout separating the system engine, backend services, documentation, and development infrastructure.

Typical structure:

```
system-performance-visualizer
│
├── src/                # C++ system monitoring engine
├── backend/            # FastAPI backend service
├── docs/               # Project documentation
│   ├── viva/           # Viva preparation notes
│   ├── development/    # Development rules and workflow
│   ├── plan/           # Plan of action
│   └── proposals/      # Architecture and design documents
├── scripts/            # Build and automation scripts
├── .devcontainer/      # Dev container configuration
├── README.md           # Project overview
└── .gitignore          # Git ignore rules
```

This structure ensures clear separation between the system engine, web backend, documentation, and development infrastructure.

## Academic Context

This project is developed as a Major Project for the Bachelor of Computer Applications (BCA) program under the Panjab University syllabus.

## Viva Preparation

All viva-related questions and answers are maintained here:

* [Viva Notes](docs/viva/README.md)

## Development Notes

Development rules and workflow are documented here:

* [Development Rules](docs/development/README.md)

## Project Plan

The detailed development roadmap is available here:

* [Plan of Action](docs/plan/planOfAction.md)

## Status

🚧 In development
