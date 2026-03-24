```mermaid
flowchart LR

    User["User"]
    System["System Performance Visualizer"]
    Kernel["Linux /proc Filesystem"]

    User -->|Request System Statistics| System
    System -->|Display CPU & Memory Usage| User
    System -->|Read System Data| Kernel
    Kernel -->|Return System Metrics| System
```
