# Plan of Action – System Performance Visualizer

This document describes the structured plan followed for the development of the
**System Performance Visualizer** project.
The plan ensures systematic progress, clear milestones, and academic alignment.

---

## 1. Project Objective

The objective of this project is to design and implement a **cloud-based web
application** that visualizes real-time system performance metrics such as CPU
and memory usage, and demonstrates operating system concepts like CPU scheduling
and memory management.

The project combines:

* Low-level system programming
* Web application development
* Cloud deployment

---

## 2. Project Scope

### Included in Scope

* Real CPU usage monitoring using Linux `/proc/stat`
* Real memory usage monitoring using Linux `/proc/meminfo`
* Web-based dashboard for visualization
* Deployment on a Linux cloud virtual machine
* CPU scheduling and memory allocation simulations
* Controlled load generation for demonstration purposes

### Excluded from Scope

* Kernel modification
* Real-time OS guarantees
* Monitoring of remote client machines
* Serverless cloud platforms

---

## 3. Technology Stack Overview

| Layer           | Technology                  |
| --------------- | --------------------------- |
| System Core     | C++                         |
| OS              | Linux                       |
| Web Backend     | Python (FastAPI)            |
| Web Server      | Uvicorn                     |
| Frontend        | HTML, CSS, JavaScript       |
| Deployment      | Linux Cloud VM              |
| Version Control | Git & GitHub                |
| Dev Environment | Dev Containers + Codespaces |

---

## 4. Development Phases

### Phase 1: Project Setup & Foundation (Completed)

**Activities**

* Repository initialization
* Git workflow setup
* Documentation structure creation
* Development rules definition

**Deliverables**

* Clean repository structure
* Development guidelines
* Initial documentation

---

### Phase 2: System Monitoring Engine (Completed)

**Activities**

* Design of system monitor abstraction
* Implementation of memory usage monitoring
* Implementation of CPU usage calculation using `/proc/stat`
* Validation through stress testing

**Deliverables**

* C++ system monitoring engine
* Verified CPU and memory metrics
* Related viva documentation

---

### Phase 3: Architecture & Design Documentation (Completed)

**Activities**

* Technology stack justification
* System architecture design
* Layered architecture definition
* Documentation indexing and navigation

**Deliverables**

* Design decision documents
* Architecture explanation
* Indexed viva notes

---

### Phase 4: Web Backend Development (In Progress)

**Activities**

* Create Python web backend skeleton
* Expose REST APIs for CPU and memory metrics
* Integrate C++ engine with Python backend
* Return system statistics in JSON format

**Deliverables**

* Working web backend
* API endpoint `/api/stats`

---

### Phase 5: Web Frontend Development (Planned)

**Activities**

* Build basic web dashboard
* Implement polling mechanism for live updates
* Display CPU and memory charts
* Ensure browser compatibility

**Deliverables**

* Functional web UI
* Live updating system metrics

---

### Phase 6: Scheduling & Memory Simulation (Planned)

**Activities**

* Implement FCFS scheduling simulation
* Visualize scheduling results
* Implement basic memory allocation strategies
* Show fragmentation behavior

**Deliverables**

* Scheduling simulation module
* Memory allocation simulation module

---

### Phase 7: Load Generation Feature (Planned)

**Activities**

* Add controlled CPU load generation
* Add controlled memory load generation
* Auto-reset load after fixed duration
* Integrate controls in web UI

**Deliverables**

* Demonstration-ready load generation
* Safe and reversible stress testing

---

### Phase 8: Cloud Deployment (Planned)

**Activities**

* Provision Linux cloud VM
* Deploy backend and C++ engine
* Configure ports and firewall rules
* Test access via public IP

**Deliverables**

* Fully cloud-hosted web application
* Deployment instructions

---

### Phase 9: Testing & Validation (Planned)

**Activities**

* Functional testing of APIs
* UI behavior testing
* Stress testing verification
* Error handling checks

**Deliverables**

* Verified stable application
* Test observations

---

### Phase 10: Finalization & Submission (Planned)

**Activities**

* Screenshot capture
* Final README update
* Report alignment with implementation
* Demo preparation

**Deliverables**

* Submission-ready project
* Viva-ready documentation

---

## Development Environment Setup

Completed:

* Configured Dev Container environment
* Added GitHub Codespaces support
* Implemented automated build script
* Introduced Python virtual environment for backend dependencies

---

## 5. Version Control Strategy

* GitHub is used as the single source of truth
* Development is done in logical commits
* Documentation and code changes are committed separately
* Sensitive files are excluded using `.gitignore`

---

## 6. Deployment Strategy

* The application is deployed on a Linux cloud virtual machine
* The system monitors the host cloud server itself
* Access is provided via web browser using public IP

---

## 7. Current Project Status

**Completed Phases:**

* Phase 1: Setup & Foundation
* Phase 2: System Monitoring Engine
* Phase 3: Architecture & Design Documentation

**In Progress:**

* Phase 4: Web Backend Development

---

## 8. Conclusion

This plan ensures that the project is developed in a structured, incremental,
and academically sound manner while meeting the requirements of a web-based,
cloud-deployed application.
