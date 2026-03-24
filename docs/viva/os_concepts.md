# Operating System Concepts (Viva Notes)

- [Operating System Concepts (Viva Notes)](#operating-system-concepts-viva-notes)
  - [Q: What is CPU scheduling?](#q-what-is-cpu-scheduling)
    - [Explanation](#explanation)
    - [One-line viva answer](#one-line-viva-answer)
  - [Q: Why does this project simulate scheduling instead of controlling real scheduling?](#q-why-does-this-project-simulate-scheduling-instead-of-controlling-real-scheduling)
    - [Explanation](#explanation-1)
    - [Academic justification](#academic-justification)
    - [One-line viva answer](#one-line-viva-answer-1)
  - [Q: Which scheduling algorithms are implemented?](#q-which-scheduling-algorithms-are-implemented)
    - [Implemented algorithms](#implemented-algorithms)
    - [Educational value](#educational-value)
    - [One-line viva answer](#one-line-viva-answer-2)
  - [Q: What is the difference between preemptive and non-preemptive scheduling?](#q-what-is-the-difference-between-preemptive-and-non-preemptive-scheduling)
    - [Explanation](#explanation-2)
    - [Key distinction](#key-distinction)
    - [One-line viva answer](#one-line-viva-answer-3)
  - [Q: What is memory fragmentation?](#q-what-is-memory-fragmentation)
    - [Explanation](#explanation-3)
    - [One-line viva answer](#one-line-viva-answer-4)
  - [Q: Why simulate memory allocation?](#q-why-simulate-memory-allocation)
    - [Explanation](#explanation-4)
    - [Educational benefit](#educational-benefit)
    - [One-line viva answer](#one-line-viva-answer-5)
  - [Q: What is FCFS scheduling?](#q-what-is-fcfs-scheduling)
  - [Q: How are scheduling parameters calculated?](#q-how-are-scheduling-parameters-calculated)
  - [Q: Why does CPU remain idle in FCFS?](#q-why-does-cpu-remain-idle-in-fcfs)
  - [Q: Why is sorting required in FCFS?](#q-why-is-sorting-required-in-fcfs)


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

---

## Q: What is FCFS scheduling?

**A:**

FCFS (First Come First Serve) is a non-preemptive scheduling algorithm where processes are executed in the order of their arrival time.

**One-line:**

> “FCFS executes processes in arrival order without preemption.”

---

## Q: How are scheduling parameters calculated?

**A:**

* Completion Time = finish time
* Turnaround Time = Completion − Arrival
* Waiting Time = Turnaround − Burst

**One-line:**

> “TAT = CT − AT and WT = TAT − BT.”

---

## Q: Why does CPU remain idle in FCFS?

**A:**

If no process has arrived, the CPU remains idle until the first process enters the ready queue.

**One-line:**

> “CPU stays idle if no process is available.”

---

## Q: Why is sorting required in FCFS?

**A:**

Sorting ensures processes are executed in order of arrival time, which is the core principle of FCFS.

**One-line:**

> “Sorting enforces correct execution order.”

---