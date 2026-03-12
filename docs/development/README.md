# Development Notes & Rules

This document defines the rules followed throughout the development of the **System Performance Visualizer** project. These rules ensure code quality, stability, and seamless development across multiple systems.

---

## Development Workflow

The project is designed to support development across multiple systems without requiring repeated installation of tools and dependencies.

To achieve this, the repository includes a **Dev Container configuration** and supports **GitHub Codespaces**.

The development container provides:

* Linux development environment
* C++ compiler (g++)
* Python runtime
* FastAPI backend dependencies
* Preconfigured VS Code extensions

When a Codespace starts, the container automatically installs the required tools and prepares the development environment. This ensures that the development environment remains consistent across machines.

Developers can work either:

* Locally using WSL/Linux
* Using GitHub Codespaces directly from a browser

---

## Version Control Rules

1. GitHub is the single source of truth for the project
2. All changes must be committed before switching systems
3. One logical change must correspond to one commit
4. Always pull the latest changes before starting work
5. Never edit code directly on the GitHub website

---

## Branching Rules

6. `main` branch represents stable, demo-ready code
7. Active development is done on the `development` branch
8. Code is merged into `main` only after testing

---

## Code Organization Rules

9. Core logic must remain independent of GUI code
10. OS-specific code must be isolated behind interfaces
11. Header files declare interfaces; source files contain implementations
12. No business logic is allowed inside GUI classes

---

## Security & Environment Rules

13. Sensitive files such as `.env.local` must never be committed
14. Environment-specific files must be listed in `.gitignore`
15. Credentials and tokens are stored locally only

---

## Commit Discipline Rules

16. Commit messages must be descriptive and meaningful
17. Temporary or experimental code must not be committed
18. Broken or untested code must never be pushed

---

## General Discipline Rules

19. No unnecessary files or folders should be added to the repository
20. Documentation must be updated when design decisions change

---

## Project Planning Discipline

The **Plan of Action** document is treated as a living document and must be kept up to date.

The Plan of Action must be updated whenever:

* A development phase is completed
* A new major feature is added
* Scope or implementation details change
* Architectural decisions are revised

This ensures that the repository always reflects the current state of the project and provides a clear progress trail.

---

## Ignored Files

The following files are excluded from version control:

* `.venv/` – Python virtual environment
* `bin/` – compiled binaries
* `.env` – environment variables

---

## Commit Tracking

Major development milestones are recorded using Git commits.

Examples include:

* C++ monitoring engine implementation
* CPU usage calculation using `/proc/stat`
* FastAPI backend integration
* Dev container environment setup

---

## Repository Structure Reference

The project follows a structured repository layout separating core logic, backend services, documentation, and development tooling.

Typical structure:

```
system-performance-visualizer
│
├── src/                # C++ system monitoring engine
├── backend/            # FastAPI backend service
├── docs/               # Project documentation
│   ├── viva/           # Viva preparation notes
│   ├── development/    # Development rules and workflow
│   ├── plan/           # Plan of action
│   └── proposals/      # Architecture and design documents
├── scripts/            # Build and automation scripts
├── .devcontainer/      # Dev container configuration
├── README.md           # Project overview
└── .gitignore          # Git ignore rules
```

This structure ensures clear separation between the system engine, web backend, documentation, and development infrastructure.

---

These rules are mandatory and followed for the entire duration of the project.
