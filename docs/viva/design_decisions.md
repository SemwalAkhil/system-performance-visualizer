# Design Decisions (Viva Notes)

## Decision: Use Linux instead of Windows

**Reason:**  
Linux exposes system performance data through the `/proc` filesystem, which aligns closely with operating system concepts taught in the syllabus.

---

### Explanation

- Linux provides CPU, memory, and process information via `/proc`
- This data can be accessed using standard file I/O
- No special permissions or proprietary APIs are required

In contrast, Windows requires complex system APIs that are less aligned with academic OS concepts.

---

### Academic benefit

- Direct mapping to OS syllabus topics
- Easier explanation during viva
- Clear visibility of kernel-maintained data

---

### One-line viva answer

> “Linux was chosen because it exposes system performance data through `/proc`, which aligns well with OS concepts.”

---

## Decision: Use WSL instead of dual boot

**Reason:**  
WSL provides a real Linux kernel environment without the risks and overhead of disk partitioning.

---

### Explanation

- WSL2 runs a genuine Linux kernel
- `/proc` behaves the same as native Linux
- No need to reboot or manage multiple OS installations

This makes development safer and more convenient.

---

### Practical advantage

- Faster setup
- No risk of data loss
- Easy switching between Windows tools and Linux environment

---

### One-line viva answer

> “WSL was used because it provides a real Linux environment without the risks of dual booting.”

---

## Decision: Use interface-based design

**Reason:**  
Interface-based design allows OS-specific implementations without affecting core logic or GUI.

---

### Explanation

- `SystemMonitor` defines a common interface
- `LinuxSystemMonitor` provides Linux-specific behavior
- GUI and core logic depend only on the interface

This avoids tight coupling between modules.

---

### Design benefit

- Improved modularity
- Easier testing
- Future extensibility (e.g., Windows support)

---

### One-line viva answer

> “Interface-based design separates OS-specific code from core logic and GUI.”

---

## Decision: Separate core logic from GUI

**Reason:**  
Separating core logic from the GUI improves testability and follows the principle of separation of concerns.

---

### Explanation

- Core modules handle algorithms and system logic
- GUI modules handle user interaction and visualization
- Each part can be developed and tested independently

This prevents mixing business logic with presentation logic.

---

### Software engineering principle

- Separation of concerns
- Clean architecture
- Easier maintenance

---

### One-line viva answer

> “Core logic and GUI are separated to improve modularity and testability.”

---

## Decision: Start with memory monitoring before CPU monitoring

**Reason:**  
Memory usage is deterministic and can be calculated from a single data source, while CPU usage requires time-based sampling.

---

### Explanation

- Memory usage can be computed from `/proc/meminfo`
- CPU usage requires two readings from `/proc/stat`
- Time difference is needed to calculate CPU percentage

Starting with memory monitoring reduces complexity during initial development.

---

### Development advantage

- Easier debugging
- Incremental progress
- Cleaner implementation

---

### One-line viva answer

> “Memory monitoring was implemented first because it is deterministic, unlike CPU usage which requires time-based sampling.”
