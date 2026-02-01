# Operating System Concepts (Viva Notes)

## Q: What is CPU scheduling?

**A:**  
CPU scheduling is the operating system mechanism that decides **which process gets access to the CPU** when multiple processes are ready to execute.

---

### Explanation

- The CPU is a shared resource
- Multiple processes may be in the ready state at the same time
- The OS scheduler selects one process based on a scheduling algorithm

The goal is to:

- Maximize CPU utilization
- Minimize waiting time
- Ensure fairness among processes

---

### One-line viva answer

> “CPU scheduling decides which ready process gets CPU time.”

---

## Q: Why does this project simulate scheduling instead of controlling real scheduling?

**A:**  
The project simulates scheduling because **real CPU scheduling is controlled by the kernel** and cannot be safely modified by user-space programs.

---

### Explanation

- Real scheduling occurs in kernel mode
- User programs run in user mode
- Allowing user programs to control scheduling would compromise system stability and security

Therefore, scheduling is **simulated** to demonstrate algorithm behavior without affecting the real system.

---

### Academic justification

- Simulation is sufficient to understand algorithm logic
- Aligns with OS syllabus requirements
- Avoids unsafe kernel-level operations

---

### One-line viva answer

> “Scheduling is simulated because real scheduling is kernel-controlled and unsafe to modify from user space.”

---

## Q: Which scheduling algorithms are implemented?

**A:**  
The project implements the following CPU scheduling algorithms:

---

### Implemented algorithms

- **FCFS (First Come First Serve)**  
  Processes are executed in the order of arrival.

- **SJF (Shortest Job First)**  
  The process with the shortest CPU burst time is selected first.

- **Priority Scheduling**  
  The process with the highest priority is scheduled first.

- **Round Robin**  
  Each process is given a fixed time slice in a cyclic order.

---

### Educational value

These algorithms represent different scheduling strategies and trade-offs.

---

### One-line viva answer

> “FCFS, SJF, Priority Scheduling, and Round Robin are implemented.”

---

## Q: What is the difference between preemptive and non-preemptive scheduling?

**A:**  
The difference lies in whether a running process can be **interrupted**.

---

### Explanation

- **Preemptive scheduling**

  - The OS can interrupt a running process
  - CPU can be reassigned to another process
  - Example: Round Robin

- **Non-preemptive scheduling**
  - A process runs until completion or blocking
  - No forced interruption
  - Example: FCFS

---

### Key distinction

Preemptive scheduling improves responsiveness, while non-preemptive scheduling is simpler.

---

### One-line viva answer

> “Preemptive scheduling allows interruption of processes; non-preemptive scheduling does not.”

---

## Q: What is memory fragmentation?

**A:**  
Memory fragmentation refers to **wasted memory space** that occurs due to inefficient allocation of memory blocks.

---

### Explanation

- **Internal fragmentation**

  - Allocated memory is larger than required
  - Unused space remains inside allocated blocks

- **External fragmentation**
  - Free memory exists but is non-contiguous
  - Cannot be allocated to larger requests

Both reduce effective memory utilization.

---

### One-line viva answer

> “Memory fragmentation is wasted memory caused by non-contiguous or inefficient allocation.”

---

## Q: Why simulate memory allocation?

**A:**  
Memory allocation is simulated because **real memory management is handled by the kernel** and cannot be modified by user-space applications.

---

### Explanation

- Real memory allocation involves kernel-level data structures
- Modifying it from user space would be unsafe
- Simulation allows visualization without affecting the system

The project demonstrates allocation strategies such as:

- First Fit
- Best Fit

---

### Educational benefit

- Helps understand memory management concepts
- Visualizes fragmentation and allocation behavior
- Reinforces theoretical learning

---

### One-line viva answer

> “Memory allocation is simulated because real memory management is kernel-controlled.”
