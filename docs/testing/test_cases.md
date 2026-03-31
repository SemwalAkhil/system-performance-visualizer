# Test Case Report

## Project: Cloud-Based System Performance Visualizer

---

## 1. Objective

The purpose of testing is to verify that all components of the system—
including the FastAPI backend, C++ monitoring engine, scheduler module,
and frontend integration—work correctly and produce expected results.

---

## 2. Test Cases

### 2.1 System Monitoring API

| Test Case ID    | TC-01                            |
| --------------- | -------------------------------- |
| Feature         | Fetch System Stats               |
| Endpoint        | `/api/stats`                     |
| Input           | GET request                      |
| Expected Output | JSON with CPU and Memory usage   |
| Actual Output   | JSON response received correctly |
| Status          | ✅ Pass                           |

---

| Test Case ID    | TC-02                     |
| --------------- | ------------------------- |
| Feature         | CPU Usage Validity        |
| Input           | Continuous API calls      |
| Expected Output | CPU value between 0–100%  |
| Actual Output   | Values within valid range |
| Status          | ✅ Pass                    |

---

| Test Case ID    | TC-03                               |
| --------------- | ----------------------------------- |
| Feature         | Memory Usage Validity               |
| Input           | GET `/api/stats`                    |
| Expected Output | Memory usage > 0 and < total memory |
| Actual Output   | Correct memory values returned      |
| Status          | ✅ Pass                              |

---

### 2.2 Scheduler Module

| Test Case ID    | TC-04                                 |
| --------------- | ------------------------------------- |
| Feature         | FCFS Scheduling                       |
| Input           | Processes with arrival & burst times  |
| Expected Output | Execution order based on arrival time |
| Actual Output   | Matches FCFS logic                    |
| Status          | ✅ Pass                                |

---

| Test Case ID    | TC-05                         |
| --------------- | ----------------------------- |
| Feature         | FCFS Waiting Time Calculation |
| Input           | Multiple processes            |
| Expected Output | Correct waiting time values   |
| Actual Output   | Values computed correctly     |
| Status          | ✅ Pass                        |

---

| Test Case ID    | TC-06                    |
| --------------- | ------------------------ |
| Feature         | FCFS Turnaround Time     |
| Input           | Process list             |
| Expected Output | Correct turnaround times |
| Actual Output   | Matches expected values  |
| Status          | ✅ Pass                   |

---

| Test Case ID    | TC-07                           |
| --------------- | ------------------------------- |
| Feature         | Invalid Input Handling          |
| Input           | Empty or malformed process data |
| Expected Output | No crash, safe handling         |
| Actual Output   | System remains stable           |
| Status          | ✅ Pass                          |

---

### 2.3 Load Generation

| Test Case ID    | TC-08                     |
| --------------- | ------------------------- |
| Feature         | CPU Load Generation       |
| Input           | Trigger load generation   |
| Expected Output | CPU usage increases       |
| Actual Output   | CPU usage spikes observed |
| Status          | ✅ Pass                    |

---

| Test Case ID    | TC-09                       |
| --------------- | --------------------------- |
| Feature         | Stop Load                   |
| Input           | Stop load command           |
| Expected Output | CPU usage returns to normal |
| Actual Output   | CPU stabilizes              |
| Status          | ✅ Pass                      |

---

### 2.4 Frontend Integration

| Test Case ID    | TC-10                     |
| --------------- | ------------------------- |
| Feature         | Chart Rendering           |
| Input           | API data                  |
| Expected Output | Graph updates dynamically |
| Actual Output   | Charts update correctly   |
| Status          | ✅ Pass                    |

---

| Test Case ID    | TC-11                  |
| --------------- | ---------------------- |
| Feature         | Real-time Updates      |
| Input           | Continuous polling     |
| Expected Output | Smooth graph updates   |
| Actual Output   | Data updates correctly |
| Status          | ✅ Pass                 |

---

### 2.5 Deployment Testing

| Test Case ID    | TC-12                        |
| --------------- | ---------------------------- |
| Feature         | Cloud Deployment             |
| Input           | Access via public IP         |
| Expected Output | Dashboard loads successfully |
| Actual Output   | Application accessible       |
| Status          | ✅ Pass                       |

---

| Test Case ID    | TC-13                  |
| --------------- | ---------------------- |
| Feature         | API Accessibility      |
| Input           | External API request   |
| Expected Output | Valid JSON response    |
| Actual Output   | API responds correctly |
| Status          | ✅ Pass                 |

---

## 3. Summary

All major components of the system were tested, including:

- System monitoring APIs
- Scheduling algorithms
- Load generation
- Frontend visualization
- Cloud deployment

All test cases passed successfully, confirming that the system is stable,
functional, and meets the project requirements.

---