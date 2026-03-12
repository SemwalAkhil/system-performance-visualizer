# Design Decisions (Viva Notes)

- [Design Decisions (Viva Notes)](#design-decisions-viva-notes)
  - [Decision: Use Linux instead of Windows](#decision-use-linux-instead-of-windows)
    - [Explanation](#explanation)
    - [Academic benefit](#academic-benefit)
    - [One-line viva answer](#one-line-viva-answer)
  - [Decision: Use WSL instead of dual boot](#decision-use-wsl-instead-of-dual-boot)
    - [Explanation](#explanation-1)
    - [Practical advantage](#practical-advantage)
    - [One-line viva answer](#one-line-viva-answer-1)
  - [Decision: Use interface-based design](#decision-use-interface-based-design)
    - [Explanation](#explanation-2)
    - [Design benefit](#design-benefit)
    - [One-line viva answer](#one-line-viva-answer-2)
  - [Decision: Separate core logic from GUI](#decision-separate-core-logic-from-gui)
    - [Explanation](#explanation-3)
    - [Software engineering principle](#software-engineering-principle)
    - [One-line viva answer](#one-line-viva-answer-3)
  - [Decision: Start with memory monitoring before CPU monitoring](#decision-start-with-memory-monitoring-before-cpu-monitoring)
    - [Explanation](#explanation-4)
    - [Development advantage](#development-advantage)
    - [One-line viva answer](#one-line-viva-answer-4)
  - [Q: Why was the project converted from a desktop application to a web application?](#q-why-was-the-project-converted-from-a-desktop-application-to-a-web-application)
    - [One-line viva answer](#one-line-viva-answer-5)
  - [Q: Why is the system monitoring engine implemented in C++ instead of Python?](#q-why-is-the-system-monitoring-engine-implemented-in-c-instead-of-python)
    - [One-line viva answer](#one-line-viva-answer-6)
  - [Q: Why was FastAPI chosen for the web backend?](#q-why-was-fastapi-chosen-for-the-web-backend)
    - [One-line viva answer](#one-line-viva-answer-7)
  - [Q: Why is the project using a layered architecture?](#q-why-is-the-project-using-a-layered-architecture)
    - [One-line viva answer](#one-line-viva-answer-8)
  - [Q: Why is the Linux `/proc` filesystem used for monitoring?](#q-why-is-the-linux-proc-filesystem-used-for-monitoring)
    - [One-line viva answer](#one-line-viva-answer-9)
  - [Q: Why is a Python virtual environment used?](#q-why-is-a-python-virtual-environment-used)
    - [One-line viva answer](#one-line-viva-answer-10)
  - [Q: Why was GitHub Codespaces used for development?](#q-why-was-github-codespaces-used-for-development)
    - [One-line viva answer](#one-line-viva-answer-11)
  - [Q: What is the purpose of a Dev Container in this project?](#q-what-is-the-purpose-of-a-dev-container-in-this-project)
    - [One-line viva answer](#one-line-viva-answer-12)
  - [Q: Why was an automated build script (`build.sh`) created?](#q-why-was-an-automated-build-script-buildsh-created)
    - [One-line viva answer](#one-line-viva-answer-13)
  - [Q: Why are compiled binaries ignored in `.gitignore`?](#q-why-are-compiled-binaries-ignored-in-gitignore)
    - [One-line viva answer](#one-line-viva-answer-14)
  - [Q: Why was a Dev Container introduced in the project?](#q-why-was-a-dev-container-introduced-in-the-project)
    - [One-line viva answer](#one-line-viva-answer-15)
  - [Q: Why is GitHub Codespaces used for development?](#q-why-is-github-codespaces-used-for-development)
    - [One-line viva answer](#one-line-viva-answer-16)
  - [Q: Why is a build script used instead of compiling manually?](#q-why-is-a-build-script-used-instead-of-compiling-manually)
    - [One-line viva answer](#one-line-viva-answer-17)
  - [Q: Why are compiled binaries stored in the `bin` directory?](#q-why-are-compiled-binaries-stored-in-the-bin-directory)
    - [One-line viva answer](#one-line-viva-answer-18)
  - [Q: Why was a repository structure created with separate directories for `src`, `backend`, and `docs`?](#q-why-was-a-repository-structure-created-with-separate-directories-for-src-backend-and-docs)
    - [One-line viva answer](#one-line-viva-answer-19)


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

---

## Q: Why was the project converted from a desktop application to a web application?

**A:**
Initially the project was planned as a desktop application using Qt for GUI. However, the project supervisor required the final submission to be a web application.

To meet this requirement while preserving the system programming component, the architecture was redesigned:

* The **system monitoring engine remains in C++**
* A **Python FastAPI backend exposes system statistics through REST APIs**
* A **web interface consumes the API and displays system metrics**

This design keeps the low-level OS interaction while fulfilling the web application requirement.

### One-line viva answer

> “The project was converted to a web application to meet academic requirements while preserving the C++ system monitoring engine through a FastAPI backend.”

---

## Q: Why is the system monitoring engine implemented in C++ instead of Python?

**A:**
C++ was chosen because the project focuses on operating system concepts and low-level system interaction.

C++ provides:

* Direct control over system-level operations
* High performance for repeated metric calculations
* Better alignment with OS-level programming concepts

The engine directly reads system statistics from the Linux `/proc` filesystem.

Python is used only as the **web interface layer**, not for the core monitoring logic.

### One-line viva answer

> “C++ is used for the system engine because it provides efficient low-level access to OS data.”

---

## Q: Why was FastAPI chosen for the web backend?

**A:**
FastAPI was selected because it is lightweight, modern, and optimized for building APIs.

Key advantages:

* High performance due to ASGI support
* Automatic API documentation
* Native JSON handling
* Easy integration with Python scripts

Since the backend only exposes system statistics through APIs, FastAPI provides a clean and minimal solution.

### One-line viva answer

> “FastAPI was chosen because it provides high-performance REST APIs with minimal overhead.”

---

## Q: Why is the project using a layered architecture?

**A:**
The system is divided into three layers:

1. Client Layer – Web browser dashboard
2. Application Layer – FastAPI backend
3. System Layer – C++ monitoring engine

This separation ensures:

* modular design
* easier testing
* independent development of components

Each layer performs a specific responsibility without interfering with others.

### One-line viva answer

> “Layered architecture separates the client interface, backend logic, and system monitoring engine.”

---

## Q: Why is the Linux `/proc` filesystem used for monitoring?

**A:**
The `/proc` filesystem is a virtual filesystem provided by the Linux kernel that exposes system and process information.

Important files used:

* `/proc/stat` → CPU statistics
* `/proc/meminfo` → memory statistics

These files provide real-time kernel data that can be read using standard file I/O.

### One-line viva answer

> “The `/proc` filesystem provides real-time kernel statistics for CPU and memory usage.”

---

## Q: Why is a Python virtual environment used?

**A:**
A Python virtual environment isolates project dependencies from the global system environment.

Benefits include:

* avoiding version conflicts
* keeping project dependencies minimal
* improving reproducibility across machines

The project creates a `.venv` directory and installs backend dependencies using `requirements.txt`.

### One-line viva answer

> “A virtual environment isolates project dependencies and prevents conflicts with system Python packages.”

---

## Q: Why was GitHub Codespaces used for development?

**A:**
The development environment needed to work across multiple college computers without repeated setup.

GitHub Codespaces provides:

* a cloud-based development environment
* automatic installation of dependencies
* consistent configuration using dev containers

This allows the project to be developed from any browser.

### One-line viva answer

> “GitHub Codespaces allows development from any system without installing local dependencies.”

---

## Q: What is the purpose of a Dev Container in this project?

**A:**
A Dev Container defines a reproducible development environment using Docker.

The container installs:

* C++ compiler
* Python runtime
* FastAPI dependencies
* required VS Code extensions

This ensures all developers use the same environment.

### One-line viva answer

> “Dev Containers ensure a consistent development environment across machines.”

---

## Q: Why was an automated build script (`build.sh`) created?

**A:**
The project includes a build script to automate compilation of the C++ monitoring engine.

The script:

* creates the `bin` directory
* compiles the monitoring engine
* generates the executable binary

This simplifies environment setup and ensures the project builds consistently.

### One-line viva answer

> “The build script automates compilation of the C++ system monitoring engine.”

---

## Q: Why are compiled binaries ignored in `.gitignore`?

**A:**
Compiled binaries are platform-dependent and can be recreated from source code.

Committing them would:

* increase repository size
* cause conflicts between different systems
* reduce reproducibility

Therefore only source code is tracked.

### One-line viva answer

> “Compiled binaries are ignored because they can be recreated from source and are platform dependent.”

---

## Q: Why was a Dev Container introduced in the project?

**A:**
The development environment had to work across multiple college computers where the system configuration changes frequently. Installing tools such as Git, Python, compilers, and dependencies repeatedly was inefficient.

A Dev Container was introduced to define a **portable development environment** using Docker. The container automatically installs required tools such as the C++ compiler, Python runtime, and project dependencies.

This ensures that the development environment is identical across different machines.

### One-line viva answer

> “Dev Containers provide a portable and reproducible development environment across multiple systems.”

---

## Q: Why is GitHub Codespaces used for development?

**A:**
GitHub Codespaces allows the project to be developed directly in the browser using a preconfigured container environment.

This eliminates the need to install development tools on local machines and ensures consistent configuration.

Since the college computers change frequently, Codespaces allows the project to be accessed and developed from any system with a browser.

### One-line viva answer

> “GitHub Codespaces enables development from any system without local environment setup.”

---

## Q: Why is a build script used instead of compiling manually?

**A:**
Manually compiling the C++ engine using long commands can lead to errors and inconsistent builds.

A build script (`scripts/build.sh`) automates the compilation process by executing the correct compiler command and generating the executable binary.

This ensures consistent builds across development environments.

### One-line viva answer

> “The build script automates compilation of the C++ monitoring engine.”

---

## Q: Why are compiled binaries stored in the `bin` directory?

**A:**
Compiled executables are stored in the `bin` directory to separate source code from build outputs.

This improves project organization and prevents accidental modification of compiled files.

The directory is also ignored by Git because binaries can be regenerated.

### One-line viva answer

> “The `bin` directory separates compiled binaries from source code.”

---

## Q: Why was a repository structure created with separate directories for `src`, `backend`, and `docs`?

**A:**
Separating the repository into structured directories improves maintainability and clarity.

Each directory has a specific purpose:

* `src` contains the C++ system monitoring engine
* `backend` contains the web backend implementation
* `docs` contains project documentation

This separation makes the project easier to navigate and maintain.

### One-line viva answer

> “Structured directories separate system code, backend services, and documentation.”

---
