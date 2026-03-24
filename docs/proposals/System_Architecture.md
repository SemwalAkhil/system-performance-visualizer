# System Architecture

## Architectural Overview

The **System Performance Visualizer** follows a layered client–server architecture. The system is divided into three primary layers:

1. Presentation Layer (Client)
2. Application Layer (Web Backend)
3. System Layer (C++ Engine interacting with the Linux kernel)

This layered architecture ensures clear separation of responsibilities, easier maintainability, and modular development.

---

## System Architecture Diagram

The full architecture diagram is maintained separately to keep this document clean.

➡ View diagram: [System Architecture Diagram](../diagrams/system_architecture.md)

---

## Component Description

### Web Browser (Client Layer)

* Sends HTTP requests to the backend API
* Receives JSON responses containing system statistics
* Displays CPU and memory usage through the web dashboard

### FastAPI Backend (Application Layer)

* Receives API requests from the browser
* Executes the compiled C++ monitoring engine
* Parses JSON output produced by the system engine
* Returns structured JSON responses to the client

### C++ System Engine (System Layer)

* Reads CPU statistics from `/proc/stat`
* Reads memory statistics from `/proc/meminfo`
* Calculates system usage metrics
* Outputs the results in JSON format

### Linux `/proc` Filesystem

* Virtual filesystem provided by the Linux kernel
* Exposes real‑time system information
* Serves as the data source for monitoring

---

## Data Flow

1. The user opens the web application in a browser.
2. The browser sends a request to the FastAPI endpoint `/api/stats`.
3. The backend executes the C++ system monitoring binary.
4. The system engine reads statistics from the Linux `/proc` filesystem.
5. The engine returns JSON output containing CPU and memory usage.
6. The backend forwards this JSON response to the browser.
7. The browser updates the dashboard with the latest system statistics.

---

## Development Infrastructure

The project includes a containerized development environment using **GitHub Dev Containers**.

This environment ensures that all required tools and dependencies are automatically installed and that the project can be developed from any machine without manual setup.

Key components include:

* Docker-based dev container
* Python virtual environment (`.venv`) for backend dependencies
* Automated C++ build script (`scripts/build.sh`)
* GitHub Codespaces for browser‑based development

This infrastructure guarantees consistent development environments across multiple systems.
