## Project Title

**Cloud-Based System Performance Visualizer**

---

## 1. Problem Statement

Modern computer systems generate large amounts of performance data such as CPU usage and memory consumption. However, most low-level system monitoring tools are command-line based and not easily accessible through web interfaces. Additionally, understanding system performance concepts like CPU scheduling and memory utilization can be difficult without visual representation.

There is a need for a web-based system that can visualize real-time performance metrics while demonstrating operating system concepts in an accessible and deployable format.

---

## 2. Proposed Solution

The proposed solution is a cloud-based web application that monitors and visualizes real-time CPU and memory usage of a Linux system.

The system consists of:

* A **C++ system engine** that reads real-time data from the Linux `/proc` filesystem.
* A **Python FastAPI backend** that exposes system statistics as REST APIs.
* A **web interface** that fetches and displays performance metrics dynamically.

The application is designed to be deployed on a Linux cloud virtual machine, where it monitors the host system itself.

---

## 3. Objectives

* To implement real-time CPU and memory monitoring using system-level programming.
* To expose system metrics through a web-based REST API.
* To deploy the application in a cloud environment.
* To demonstrate practical application of operating system concepts.

---

## 4. Key Technologies

* C++ for system-level monitoring
* Python FastAPI for backend development
* Uvicorn as ASGI server
* Linux `/proc` filesystem
* HTML, CSS, and JavaScript for frontend
* Linux Cloud Virtual Machine for deployment

---

## 5. Expected Outcome

The final outcome will be a fully functional web application that:

* Displays real-time CPU and memory usage
* Runs on a cloud-hosted Linux server
* Demonstrates system-level data processing and web integration
* Provides a structured, documented, and version-controlled implementation

---
