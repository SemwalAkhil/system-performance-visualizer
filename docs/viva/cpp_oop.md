# C++ OOP & Design (Viva Notes)

## Q: What is a vtable in C++?

**A:**  
A vtable (virtual table) is a table of function pointers used by C++ to support **runtime polymorphism** for classes with virtual functions.

---

### Explanation

- When a class contains at least one virtual function, the compiler creates a vtable
- The vtable stores addresses of the virtual functions
- Each object of the class contains a hidden pointer to this vtable

At runtime, the correct function is selected based on the object type, not the pointer type.

---

### Why it is important

- Enables dynamic dispatch
- Allows base class pointers to call derived class functions
- Essential for polymorphism

---

### One-line viva answer

> “A vtable is a compiler-generated table of function pointers used to implement runtime polymorphism.”

---

## Q: Why did the linker give an "undefined reference to vtable" error?

**A:**  
The linker error occurred because a virtual function was **declared but not defined**, preventing the compiler from generating a complete vtable.

---

### Explanation

- The compiler creates the vtable during linking
- Every virtual function must have a definition
- If even one virtual function is missing, the vtable is incomplete

In this project, `getCPUUsage()` was declared but not implemented, which caused the error.

---

### Key learning

- This is a **linker error**, not a syntax error
- It appears only in multi-file projects

---

### One-line viva answer

> “The vtable error occurred because a declared virtual function had no implementation.”

---

## Q: Why must all virtual functions be implemented?

**A:**  
All virtual functions must be implemented because the vtable requires **valid function addresses** for every virtual method.

---

### Explanation

- The vtable stores pointers to virtual functions
- Missing implementations mean missing addresses
- The linker cannot complete object layout without them

Even if a function is not used, it must still exist.

---

### Practical relevance

This ensures:

- Safe runtime dispatch
- Predictable object behavior
- Correct memory layout

---

### One-line viva answer

> “All virtual functions must be implemented so the compiler can generate a complete vtable.”

---

## Q: Why use an abstract base class (`SystemMonitor`)?

**A:**  
An abstract base class is used to **separate interface from implementation** and to enable extensibility.

---

### Explanation

In this project:

- `SystemMonitor` defines _what_ system monitoring should provide
- `LinuxSystemMonitor` defines _how_ it is implemented on Linux

This design:

- Keeps core logic OS-independent
- Prevents GUI from depending on OS-specific code

---

### Design benefits

- Cleaner architecture
- Easier testing
- Future support for Windows or macOS

---

### One-line viva answer

> “An abstract base class separates interface from implementation and improves modularity.”

---

## Q: What is polymorphism in this project?

**A:**  
Polymorphism allows a base class pointer (`SystemMonitor`) to refer to different derived implementations at runtime.

---

### Explanation

- The GUI or core logic interacts only with `SystemMonitor`
- The actual object may be `LinuxSystemMonitor`
- Function calls are resolved at runtime using the vtable

This avoids hardcoding OS-specific logic.

---

### Why it matters

- Makes the system extensible
- Reduces code duplication
- Improves maintainability

---

### One-line viva answer

> “Polymorphism allows base class pointers to invoke derived class behavior at runtime.”

---

## Q: Why is the destructor virtual?

**A:**  
The destructor is virtual to ensure **proper cleanup of derived objects** when deleted through a base class pointer.

---

### Explanation

If the destructor is not virtual:

- Only the base class destructor runs
- Derived class resources may leak

In polymorphic designs, this leads to undefined behavior.

---

### Best practice

Any class intended to be inherited should have a virtual destructor.

---

### One-line viva answer

> “A virtual destructor ensures correct object destruction in polymorphic use.”

---

## Q: Why not write everything in a single `.cpp` file?

**A:**  
Writing everything in one `.cpp` file works only for very small programs. In a structured C++ project, it is avoided because it breaks modularity, reusability, and scalability.

---

### 1. Separation of declaration and implementation

Header files (`.h`) contain declarations, while source files (`.cpp`) contain implementations.

This separation:

- Makes the code easier to understand
- Allows developers to see **what a module does** without reading **how it does it**
- Improves maintainability

---

### 2. Required for multi-file compilation

This project is divided into multiple source files:

- `main.cpp`
- `LinuxSystemMonitor.cpp`
- Scheduler, memory, and GUI modules

Header files allow:

- Each `.cpp` file to compile independently
- The linker to combine them into one executable

---

### 3. Enables abstraction and polymorphism

If everything were in one file:

- Interfaces would be unclear
- OS-specific code would mix with core logic
- Future extensions would be difficult

---

### 4. Improves reusability

Headers allow interfaces to be reused while implementations change independently.

---

### 5. Reduces compilation time

Only modified files are recompiled, improving build efficiency.

---

### 6. Industry and academic standard

Large software systems never use a single source file.

---

### One-line viva answer

> “Writing everything in one `.cpp` file does not scale; headers enable modular and maintainable design.”
