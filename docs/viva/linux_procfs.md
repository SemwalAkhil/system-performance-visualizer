# Linux /proc Filesystem (Viva Notes)

- [Linux /proc Filesystem (Viva Notes)](#linux-proc-filesystem-viva-notes)
  - [Q: What is the /proc filesystem?](#q-what-is-the-proc-filesystem)
    - [Explanation](#explanation)
    - [Key property](#key-property)
    - [One-line viva answer](#one-line-viva-answer)
  - [Q: Why is `/proc` used instead of system calls?](#q-why-is-proc-used-instead-of-system-calls)
    - [Explanation](#explanation-1)
    - [Academic advantage](#academic-advantage)
    - [One-line viva answer](#one-line-viva-answer-1)
  - [Q: What information is read from `/proc/meminfo`?](#q-what-information-is-read-from-procmeminfo)
    - [Explanation](#explanation-2)
    - [Why this method is preferred](#why-this-method-is-preferred)
    - [One-line viva answer](#one-line-viva-answer-2)
  - [Q: Why is `/proc/stat` read twice for CPU usage?](#q-why-is-procstat-read-twice-for-cpu-usage)
    - [Explanation](#explanation-3)
    - [Key concept](#key-concept)
    - [One-line viva answer](#one-line-viva-answer-3)
  - [Q: Does `/proc` exist in Windows?](#q-does-proc-exist-in-windows)
    - [Explanation](#explanation-4)
    - [Design implication](#design-implication)
    - [One-line viva answer](#one-line-viva-answer-4)
  - [Q: Why is WSL acceptable for this project?](#q-why-is-wsl-acceptable-for-this-project)
    - [Explanation](#explanation-5)
    - [Academic justification](#academic-justification)
    - [One-line viva answer](#one-line-viva-answer-5)
  - [Q: How is CPU usage calculated in this project?](#q-how-is-cpu-usage-calculated-in-this-project)
    - [Explanation](#explanation-6)
    - [Data source](#data-source)
    - [Formula used](#formula-used)
    - [Why delta-based calculation is required](#why-delta-based-calculation-is-required)
    - [Implementation detail](#implementation-detail)
    - [Why CPU usage sometimes shows 0%](#why-cpu-usage-sometimes-shows-0)
    - [One-line viva answer](#one-line-viva-answer-6)


## Q: What is the /proc filesystem?

**A:**  
`/proc` is a **virtual filesystem** provided by the Linux kernel that exposes real-time information about system and process states.

---

### Explanation

- `/proc` does not store data on disk
- Files are generated dynamically by the kernel
- It provides information about CPU, memory, processes, and system statistics

Each file represents kernel data structures in a readable form.

---

### Key property

- Data changes in real time
- No manual updates are required

---

### One-line viva answer

> “`/proc` is a virtual filesystem that provides real-time kernel and process information.”

---

## Q: Why is `/proc` used instead of system calls?

**A:**  
`/proc` is used because it provides a **simple, file-based interface** that can be accessed using standard file I/O operations.

---

### Explanation

- Reading `/proc` files requires no special APIs
- Can be accessed using `ifstream`, `fopen`, or shell commands
- Easier to understand and debug compared to low-level system calls

This makes it ideal for educational and monitoring applications.

---

### Academic advantage

- Clear mapping to OS concepts
- Simplifies implementation
- Avoids complex platform-specific APIs

---

### One-line viva answer

> “`/proc` is used because it provides a simple and readable interface using standard file I/O.”

---

## Q: What information is read from `/proc/meminfo`?

**A:**  
`/proc/meminfo` provides detailed information about the system’s memory usage.

---

### Explanation

In this project, the following fields are used:

- `MemTotal` → Total physical memory
- `MemAvailable` → Memory available for new applications
- `Cached` → Memory used for file caching
- `Buffers` → Memory used for kernel buffers

Memory usage is calculated using:
(MemTotal - MemAvailable) / MemTotal

---

### Why this method is preferred

- Reflects actual usable memory
- Accounts for Linux caching behavior
- More accurate than using free memory alone

---

### One-line viva answer

> “`/proc/meminfo` provides total, available, cached, and buffered memory information.”

---

## Q: Why is `/proc/stat` read twice for CPU usage?

**A:**  
CPU usage cannot be calculated from a single reading because the values in `/proc/stat` are **cumulative**.

---

### Explanation

- `/proc/stat` stores total CPU time since system boot
- CPU usage is calculated using the **difference** between two readings
- A time interval is required to measure actual usage

The formula uses:

- Total CPU time difference
- Idle CPU time difference

---

### Key concept

CPU usage = activity over time, not a static value.

---

### One-line viva answer

> “`/proc/stat` is read twice because CPU usage is calculated using time-based differences.”

---

## Q: Does `/proc` exist in Windows?

**A:**  
No, `/proc` does **not** exist in Windows.

---

### Explanation

- `/proc` is specific to Linux and Unix-like systems
- Windows uses proprietary APIs for system information
- There is no file-based equivalent to `/proc` in Windows

This is why OS-specific implementations are required.

---

### Design implication

- Platform abstraction is necessary
- OS-specific code must be isolated

---

### One-line viva answer

> “No, `/proc` is Linux-specific and does not exist in Windows.”

---

## Q: Why is WSL acceptable for this project?

**A:**  
WSL2 is acceptable because it uses a **real Linux kernel** and exposes the `/proc` filesystem identically to native Linux.

---

### Explanation

- WSL2 runs Linux inside a lightweight virtual machine
- Kernel behavior matches native Linux
- `/proc` files behave the same as on a physical Linux system

Therefore, system monitoring results are valid.

---

### Academic justification

- Matches Linux kernel behavior
- Safe and convenient development environment
- Accepted for academic system-level projects

---

### One-line viva answer

> “WSL is acceptable because it uses a real Linux kernel and exposes `/proc` like native Linux.”

---

## Q: How is CPU usage calculated in this project?

**A:**  
CPU usage is calculated using **delta-based sampling** from the `/proc/stat` file.

---

### Explanation
- `/proc/stat` provides cumulative CPU time values since system boot
- A single reading cannot represent CPU usage
- Two readings are required at different times
- CPU usage is computed from the difference between these readings

The project reads CPU statistics periodically and calculates usage based on how much time the CPU spent in idle versus active states.

---

### Data source
The first line of `/proc/stat` is used:
```

cpu  user nice system idle iowait irq softirq steal

```

From this:
- **Idle time** = `idle + iowait`
- **Total time** = sum of all fields

---

### Formula used
```

CPU Usage (%) = (1 - idle_delta / total_delta) × 100

```

Where:
- `idle_delta` = change in idle time
- `total_delta` = change in total CPU time

---

### Why delta-based calculation is required
- Values in `/proc/stat` are cumulative
- CPU usage represents activity **over time**
- Delta-based calculation reflects real usage accurately

---

### Implementation detail
- Previous CPU values (`prevTotal`, `prevIdle`) are stored as class members
- On the first call, CPU usage is returned as `0%`
- Subsequent calls return real usage values

This design is GUI-safe and avoids blocking delays.

---

### Why CPU usage sometimes shows 0%
- The system may be idle
- The sampling interval may be short
- Minimal background CPU activity in WSL

This behavior is expected and correct.

---

### One-line viva answer
> “CPU usage is calculated using delta-based sampling from `/proc/stat` by comparing idle and total CPU time differences.”
