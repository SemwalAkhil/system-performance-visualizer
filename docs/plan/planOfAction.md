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
* CPU scheduling (FCFS) simulation
* Controlled CPU load generation for demonstration

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
| Visualization   | Chart.js                    |
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
* Fix using double-read CPU calculation method
* Validation through stress testing

**Deliverables**

* C++ system monitoring engine
* Verified CPU and memory metrics
* Accurate real-time CPU measurement

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

### Phase 4: Web Backend Development (Completed)

**Activities**

* Created FastAPI backend
* Integrated C++ binaries using subprocess
* Implemented API endpoints:

  * `/api/stats`
  * `/api/scheduler`
* Added automatic C++ build on startup

**Deliverables**

* Fully functional backend
* JSON-based API communication

---

### Phase 5: Web Frontend Development (Completed)

**Activities**

* Built dashboard UI
* Integrated Chart.js for graphs
* Implemented real-time polling
* Displayed CPU and memory usage
* Split frontend into HTML, CSS, JS modules

**Deliverables**

* Functional interactive UI
* Real-time system monitoring dashboard

---

### Phase 6: Scheduling Simulation (Completed - FCFS)

**Activities**

* Implemented FCFS scheduling in C++
* Parsed JSON input using regex
* Generated scheduling metrics
* Created timeline for execution visualization
* Integrated with frontend (table + Gantt chart)

**Deliverables**

* Working FCFS scheduler
* Visual Gantt chart with animation

---

### Phase 7: Load Generation Feature (Completed)

**Activities**

* Implemented CPU load generation using `yes` processes
* Created API endpoints:

  * `/api/load/start`
  * `/api/load/stop`
* Integrated load control in frontend UI
* Verified real CPU spike in graphs

**Deliverables**

* Real system-level CPU load generation
* Fully interactive demo feature

---

### Phase 8: UI Enhancement & Integration (Completed)

**Activities**

* Redesigned UI into dashboard layout
* Added sidebar and topbar
* Improved styling using CSS
* Connected load controls with UI
* Removed fake CPU simulation logic

**Deliverables**

* Professional dashboard interface
* Fully integrated system visualization

---

### Phase 9: Cloud Deployment (Pending)

**Activities**

* Provision Linux cloud VM
* Deploy backend and C++ engine
* Configure ports and firewall rules
* Test access via public IP

**Deliverables**

* Fully cloud-hosted web application

---

### Phase 10: Testing & Validation (In Progress)

**Activities**

* Functional testing of APIs
* UI behavior testing
* Load testing verification
* Error handling checks

**Deliverables**

* Stable and verified application

---

### Phase 11: Finalization & Submission (Pending)

**Activities**

* Screenshot capture
* Final README update
* Report alignment with implementation
* Demo preparation

**Deliverables**

* Submission-ready project
* Viva-ready documentation

---

## Development Environment Standardization

The project uses **GitHub Codespaces with Dev Containers** to ensure consistent development.

This provides:

* Pre-installed compilers and tools
* Python environment setup
* Automatic dependency installation
* Automatic C++ build execution

This ensures the project can run on any machine with a browser.

---

## 5. Version Control Strategy

* GitHub is used as the single source of truth
* Development is done in logical commits
* Documentation and code changes are committed separately
* Sensitive files are excluded using `.gitignore`

---

## 6. Deployment Strategy

* The application will be deployed on a Linux cloud VM
* The system monitors the host server
* Access is provided via browser using public IP

---

## 7. Current Project Status

### ✅ Completed

* System Monitoring (CPU + Memory)
* FastAPI Backend
* Frontend Dashboard
* FCFS Scheduling Simulation
* Real CPU Load Generation
* UI Integration and Visualization

### 🔄 In Progress

* Testing and validation

### ⏳ Pending

* Cloud deployment
* Final report and submission

---

## 8. Conclusion

The project has progressed from basic system monitoring to a fully integrated
**real-time system performance visualization platform**.

It successfully demonstrates:

* Operating system concepts
* Backend-frontend integration
* Real-time data visualization
* System-level interaction using C++ and Linux

The remaining work focuses on deployment and final presentation.
