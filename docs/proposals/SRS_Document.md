# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose

This document specifies the functional and non-functional requirements of the Cloud-Based System Performance Visualizer. The system is designed to monitor and visualize real-time CPU and memory usage through a web-based interface.

### 1.2 Scope

The application will collect real-time system performance metrics using a C++ engine and expose them through a FastAPI backend. The system will be deployed on a Linux cloud virtual machine and accessed via a web browser.

---

## 2. Overall Description

### 2.1 Product Perspective

The system follows a layered architecture:

* C++ system engine for kernel-level monitoring
* FastAPI backend for API exposure
* Web client for visualization

### 2.2 User Characteristics

* Basic computer literacy
* Ability to access a web browser
* No technical expertise required

### 2.3 Operating Environment

* Linux Operating System
* Python 3.x
* C++ compiler (g++)
* Cloud virtual machine environment

---

## 3. Functional Requirements

### 3.1 Must-Have Features

1. The system shall retrieve CPU usage from `/proc/stat`.
2. The system shall retrieve memory usage from `/proc/meminfo`.
3. The system shall output data in JSON format.
4. The backend shall expose an API endpoint `/api/stats`.
5. The application shall be accessible through a web browser.
6. The system shall support deployment on a Linux cloud VM.

---

### 3.2 Could-Have Features

1. The system may include graphical visualization of CPU and memory usage.
2. The system may include controlled CPU load generation.
3. The system may include controlled memory load generation.
4. The system may simulate scheduling algorithms.
5. The system may log historical performance data.

---

## 4. Non-Functional Requirements

### 4.1 Performance

* The system shall respond to API requests within 1 second.

### 4.2 Reliability

* The system shall handle execution errors gracefully.
* The backend shall return valid JSON responses.

### 4.3 Maintainability

* The project shall follow modular design.
* Source code shall be version controlled using Git.

### 4.4 Security

* Environment configuration files shall not be committed.
* The application shall not expose sensitive system information.

---

## 5. System Constraints

* The system depends on the Linux `/proc` filesystem.
* The application requires a Linux-based deployment environment.
* Serverless hosting platforms are not suitable due to kernel access limitations.

---

## 6. Assumptions and Dependencies

* The deployment environment provides access to `/proc`.
* Python and C++ compilers are available on the server.
* Internet access is available for cloud deployment.

---
