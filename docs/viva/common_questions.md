# Common Viva Questions

## Q: Is this project platform-dependent?

**A:**  
The project is **partially platform-dependent**.

---

### Explanation

- The **core logic** (CPU scheduling simulation, memory simulation) is written in standard C++
- This part is **platform-independent**
- The **system monitoring module** depends on the operating system

In this project:

- Linux-specific monitoring is implemented using the `/proc` filesystem
- OS-specific code is isolated using the `SystemMonitor` interface

---

### Design advantage

- Core logic can run on any OS
- Only a new system monitor implementation is required for another platform

---

### One-line viva answer

> “The core logic is platform-independent; only system monitoring is OS-specific.”

---

## Q: Why is Qt chosen for GUI?

**A:**  
Qt is chosen because it provides **cross-platform GUI support** and integrates naturally with C++.

---

### Explanation

Qt offers:

- Native C++ support
- Rich GUI widgets
- Signal–slot mechanism for event handling
- Cross-platform compatibility (Linux, Windows, macOS)

It allows the GUI to remain separate from system and core logic.

---

### Academic relevance

- Matches Computer Graphics and OOP concepts
- Widely used in industry
- Suitable for desktop-based academic projects

---

### One-line viva answer

> “Qt is chosen for its cross-platform support, C++ integration, and rich GUI features.”

---

## Q: Can this project run on Windows?

**A:**  
Yes, the project **can run on Windows** with a Windows-specific implementation of the system monitoring module.

---

### Explanation

- The current implementation uses Linux `/proc` files
- Windows does not provide `/proc`
- A Windows version would use Windows APIs for CPU and memory data

Because the project uses an abstract interface (`SystemMonitor`):

- The GUI and core logic remain unchanged
- Only the monitoring module needs replacement

---

### Design benefit

This demonstrates:

- Extensibility
- Good object-oriented design
- Platform abstraction

---

### One-line viva answer

> “Yes, by implementing a Windows-specific SystemMonitor without changing the core logic.”

---

## Q: Is this a real-time system?

**A:**  
No, this project is **not a real-time system**.

---

### Explanation

- A real-time system has strict timing constraints
- This project performs monitoring and simulation
- Delays do not cause system failure

The CPU scheduling shown is **educational simulation**, not kernel-level scheduling.

---

### Important distinction

- Monitoring ≠ controlling
- Simulation ≠ real-time execution

---

### One-line viva answer

> “No, it is a monitoring and simulation tool, not a real-time operating system.”

---

## Q: How is this project useful academically?

**A:**  
The project helps bridge the gap between **theoretical OS concepts and practical understanding**.

---

### Explanation

It allows students to:

- Visualize CPU scheduling algorithms
- Understand memory usage and fragmentation
- Observe real system statistics
- Connect theory with real system behavior

This improves conceptual clarity compared to textbook-only learning.

---

### Educational value

- Strong alignment with BCA syllabus
- Enhances OS, C++, and design understanding
- Encourages system-level thinking

---

### One-line viva answer

> “It visualizes operating system concepts that are otherwise taught only theoretically.”

📌 **Goes into:** `docs/viva/common_questions.md`
(because this is a *tooling / workflow* viva-style question; you can also keep it as personal dev notes)

---

## Q: How can I view README / Markdown files in VS Code exactly as they appear on GitHub?

**A:**
By using VS Code’s **Markdown Preview** along with a **GitHub-flavored Markdown extension**, README files can be rendered almost exactly as they appear on GitHub.

---

### 1️⃣ Built-in Markdown Preview (MANDATORY)

VS Code already has this.

#### How to use:

* Open any `.md` file
* Press:

  ```
  Ctrl + Shift + V
  ```

  **OR**
* Right-click → **Open Preview**

This renders Markdown visually.

---
