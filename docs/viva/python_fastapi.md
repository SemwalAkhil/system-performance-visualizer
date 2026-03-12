- [Python and FastAPI (Viva Notes)](#python-and-fastapi-viva-notes)
  - [Q: Why was Python chosen as the web backend instead of Node.js?](#q-why-was-python-chosen-as-the-web-backend-instead-of-nodejs)
    - [Explanation](#explanation)
    - [One-line viva answer](#one-line-viva-answer)
  - [Q: Why does the Python backend execute the C++ binary instead of linking directly?](#q-why-does-the-python-backend-execute-the-c-binary-instead-of-linking-directly)
    - [Explanation](#explanation-1)
    - [One-line viva answer](#one-line-viva-answer-1)
  - [Q: Why are we using FastAPI instead of frameworks like Django or Flask?](#q-why-are-we-using-fastapi-instead-of-frameworks-like-django-or-flask)
    - [Explanation](#explanation-2)
    - [Important distinction](#important-distinction)
    - [One-line viva answer](#one-line-viva-answer-2)
  - [Q: Why is Django not suitable for this project?](#q-why-is-django-not-suitable-for-this-project)
    - [Explanation](#explanation-3)
    - [One-line viva answer](#one-line-viva-answer-3)
  - [Q: Why not use Flask for the backend?](#q-why-not-use-flask-for-the-backend)
    - [Explanation](#explanation-4)
    - [One-line viva answer](#one-line-viva-answer-4)
  - [Q: How does FastAPI work internally?](#q-how-does-fastapi-work-internally)
    - [Explanation](#explanation-5)
    - [Important components](#important-components)
    - [One-line viva answer](#one-line-viva-answer-5)
  - [Q: How does FastAPI communicate with the C++ system engine?](#q-how-does-fastapi-communicate-with-the-c-system-engine)
    - [Explanation](#explanation-6)
    - [One-line viva answer](#one-line-viva-answer-6)
  - [Q: How does FastAPI help during development and testing?](#q-how-does-fastapi-help-during-development-and-testing)
    - [Explanation](#explanation-7)
    - [One-line viva answer](#one-line-viva-answer-7)
  - [Q: What is the role of `requirements.txt` in the project?](#q-what-is-the-role-of-requirementstxt-in-the-project)
    - [Explanation](#explanation-8)
    - [One-line viva answer](#one-line-viva-answer-8)
  - [Q: Why is `requirements.txt` important for deployment?](#q-why-is-requirementstxt-important-for-deployment)
    - [Explanation](#explanation-9)
    - [One-line viva answer](#one-line-viva-answer-9)
  - [Q: What is Uvicorn?](#q-what-is-uvicorn)
    - [Explanation](#explanation-10)
    - [One-line viva answer](#one-line-viva-answer-10)
  - [Q: Why is Uvicorn required to run FastAPI?](#q-why-is-uvicorn-required-to-run-fastapi)
    - [Explanation](#explanation-11)
    - [One-line viva answer](#one-line-viva-answer-11)
  - [Q: Why is Uvicorn listed inside `requirements.txt`?](#q-why-is-uvicorn-listed-inside-requirementstxt)
    - [Explanation](#explanation-12)
    - [One-line viva answer](#one-line-viva-answer-12)
  - [Q: How do `requirements.txt` and Uvicorn work together in this project?](#q-how-do-requirementstxt-and-uvicorn-work-together-in-this-project)
    - [Explanation](#explanation-13)
    - [One-line viva answer](#one-line-viva-answer-13)
  - [Q: What is WSGI?](#q-what-is-wsgi)
    - [Explanation](#explanation-14)
    - [One-line viva answer](#one-line-viva-answer-14)
  - [Q: What are the limitations of WSGI?](#q-what-are-the-limitations-of-wsgi)
    - [Explanation](#explanation-15)
    - [One-line viva answer](#one-line-viva-answer-15)
  - [Q: What is ASGI?](#q-what-is-asgi)
    - [Explanation](#explanation-16)
    - [One-line viva answer](#one-line-viva-answer-16)
  - [Q: Why is ASGI better suited for FastAPI?](#q-why-is-asgi-better-suited-for-fastapi)
    - [Explanation](#explanation-17)
    - [One-line viva answer](#one-line-viva-answer-17)
  - [Q: What is the role of Uvicorn in ASGI-based applications?](#q-what-is-the-role-of-uvicorn-in-asgi-based-applications)
    - [Explanation](#explanation-18)
    - [One-line viva answer](#one-line-viva-answer-18)
  - [Q: How is ASGI different from WSGI?](#q-how-is-asgi-different-from-wsgi)
    - [Explanation](#explanation-19)
    - [One-line viva answer](#one-line-viva-answer-19)
  - [Q: Why is ASGI important for this project?](#q-why-is-asgi-important-for-this-project)
    - [Explanation](#explanation-20)
    - [One-line viva answer](#one-line-viva-answer-20)
  - [Q: Does Uvicorn act as a server in this project?](#q-does-uvicorn-act-as-a-server-in-this-project)
    - [Explanation](#explanation-21)
    - [Important distinction](#important-distinction-1)
    - [One-line viva answer](#one-line-viva-answer-21)
  - [Q: What are the roles and responsibilities of a server in a web application?](#q-what-are-the-roles-and-responsibilities-of-a-server-in-a-web-application)
    - [Explanation](#explanation-22)
    - [One-line viva answer](#one-line-viva-answer-22)
  - [Q: How does Uvicorn fulfill the role of a server when used with FastAPI?](#q-how-does-uvicorn-fulfill-the-role-of-a-server-when-used-with-fastapi)
    - [Explanation](#explanation-23)
    - [One-line viva answer](#one-line-viva-answer-23)
  - [Q: Why is Uvicorn required when using FastAPI?](#q-why-is-uvicorn-required-when-using-fastapi)
    - [Explanation](#explanation-24)
    - [One-line viva answer](#one-line-viva-answer-24)
  - [Q: Why don’t we explicitly use Uvicorn-like servers in Flask or Django?](#q-why-dont-we-explicitly-use-uvicorn-like-servers-in-flask-or-django)
    - [Explanation](#explanation-25)
    - [One-line viva answer](#one-line-viva-answer-25)
  - [Q: What is the difference between how FastAPI and Flask/Django are served?](#q-what-is-the-difference-between-how-fastapi-and-flaskdjango-are-served)
    - [Explanation](#explanation-26)
    - [One-line viva answer](#one-line-viva-answer-26)
  - [Q: Is Uvicorn only used in development?](#q-is-uvicorn-only-used-in-development)
    - [Explanation](#explanation-27)
    - [One-line viva answer](#one-line-viva-answer-27)
  - [Q: Why does the FastAPI backend execute the C++ binary instead of reimplementing monitoring in Python?](#q-why-does-the-fastapi-backend-execute-the-c-binary-instead-of-reimplementing-monitoring-in-python)
    - [One-line viva answer](#one-line-viva-answer-28)
  - [Q: Why does the C++ engine return JSON output?](#q-why-does-the-c-engine-return-json-output)
    - [One-line viva answer](#one-line-viva-answer-29)
  - [Q: Why is `requirements.txt` used in the backend?](#q-why-is-requirementstxt-used-in-the-backend)
    - [One-line viva answer](#one-line-viva-answer-30)
- [File: `docs/viva/linux_procfs.md`](#file-docsvivalinux_procfsmd)
  - [Q: Why are `/proc/stat` and `/proc/meminfo` used for monitoring?](#q-why-are-procstat-and-procmeminfo-used-for-monitoring)
    - [One-line viva answer](#one-line-viva-answer-31)

# Python and FastAPI (Viva Notes)

## Q: Why was Python chosen as the web backend instead of Node.js?

**A:**  
Python was chosen because it integrates more easily with C++ system programs and is simpler to deploy and explain.

---

### Explanation
- Python can directly execute or interface with C++ binaries
- It simplifies REST API development
- It is widely accepted in academic environments
- It reduces integration complexity compared to Node.js native bindings

---

### One-line viva answer
> “Python was chosen because it acts as a simple and reliable wrapper around the C++ core.”

---

## Q: Why does the Python backend execute the C++ binary instead of linking directly?
**A:**  
Executing the binary avoids complex bindings and keeps the C++ core unchanged.

---

### Explanation
- Direct linking requires additional build complexity
- Binary execution is simpler and more robust
- It reduces integration risk
- It is easier to debug and maintain

---

### One-line viva answer
> “Executing the binary simplifies integration and reduces risk.”

---

## Q: Why are we using FastAPI instead of frameworks like Django or Flask?
**A:**  
FastAPI is used because it is lightweight, fast, and better suited for building simple REST APIs for system-level projects.

---

### Explanation
- Django is a full-stack framework with ORM, authentication, and templating
- These features are unnecessary for a system monitoring backend
- Flask is lightweight but requires additional setup for validation and documentation
- FastAPI provides built-in request validation and automatic API documentation

FastAPI allows the backend to remain simple and focused on exposing system data.

---

### Important distinction
- Django → full web applications
- Flask → minimal web framework
- FastAPI → API-first framework

---

### One-line viva answer
> “FastAPI is chosen because it is lightweight, API-focused, and provides automatic documentation.”

---

## Q: Why is Django not suitable for this project?
**A:**  
Django is not suitable because it is designed for large, database-driven web applications rather than lightweight system APIs.

---

### Explanation
- Django enforces a heavy project structure
- It includes features like ORM and admin panels by default
- The project does not require databases or user authentication
- Using Django would add unnecessary complexity

---

### One-line viva answer
> “Django was avoided because it adds unnecessary overhead for a simple system monitoring API.”

---

## Q: Why not use Flask for the backend?
**A:**  
Flask was not chosen because it requires more manual configuration compared to FastAPI.

---

### Explanation
- Flask does not provide built-in request validation
- API documentation must be added manually
- FastAPI provides automatic OpenAPI documentation
- FastAPI enforces cleaner API design by default

---

### One-line viva answer
> “FastAPI reduces boilerplate and provides built-in validation and documentation.”

---

## Q: How does FastAPI work internally?
**A:**  
FastAPI works by handling HTTP requests asynchronously and mapping them to Python functions using decorators.

---

### Explanation
- Each API endpoint is defined using a Python function
- Decorators like `@app.get()` map URLs to functions
- Request and response data are automatically converted to JSON
- Data validation is handled using type hints

FastAPI uses an ASGI server to efficiently handle requests.

---

### Important components
- ASGI server (for handling requests)
- Python functions as endpoints
- JSON-based request and response handling

---

### One-line viva answer
> “FastAPI maps HTTP requests to Python functions and automatically handles JSON conversion and validation.”

---

## Q: How does FastAPI communicate with the C++ system engine?
**A:**  
FastAPI executes the compiled C++ binary and reads its JSON output.

---

### Explanation
- The backend runs the C++ binary as a subprocess
- The binary outputs CPU and memory data in JSON format
- FastAPI reads this output and returns it to the client
- This avoids tight coupling between Python and C++

---

### One-line viva answer
> “FastAPI executes the C++ binary and forwards its JSON output to the client.”

---

## Q: How does FastAPI help during development and testing?
**A:**  
FastAPI provides automatic interactive API documentation.

---

### Explanation
- FastAPI generates OpenAPI documentation automatically
- The API can be tested using a browser at `/docs`
- No external tools are required for testing endpoints
- This speeds up development and debugging

---

### One-line viva answer
> “FastAPI provides built-in interactive API documentation that simplifies testing.”

## Q: What is the role of `requirements.txt` in the project?
**A:**  
`requirements.txt` is used to list all Python dependencies required to run the backend service.

---

### Explanation
- It specifies the Python packages needed by the project
- It allows the same environment to be recreated on any system
- It ensures consistent behavior across development and deployment
- It simplifies installation using a single command

In this project, `requirements.txt` ensures that the FastAPI backend can be set up easily on local machines and cloud servers.

---

### One-line viva answer
> “`requirements.txt` lists all Python dependencies required to run the backend consistently.”

---

## Q: Why is `requirements.txt` important for deployment?
**A:**  
It allows the backend environment to be recreated reliably on another machine or cloud server.

---

### Explanation
- Cloud VMs start with a clean environment
- Dependencies are not pre-installed
- `requirements.txt` ensures all required packages are installed correctly
- It prevents version mismatch issues

This is essential for smooth cloud deployment.

---

### One-line viva answer
> “It ensures the backend can be set up reliably during deployment.”

---

## Q: What is Uvicorn?
**A:**  
Uvicorn is an ASGI server used to run FastAPI applications.

---

### Explanation
- FastAPI itself does not run a server
- Uvicorn acts as the web server that listens for HTTP requests
- It forwards incoming requests to the FastAPI application
- It handles request–response communication efficiently

---

### One-line viva answer
> “Uvicorn is the server that runs the FastAPI application.”

---

## Q: Why is Uvicorn required to run FastAPI?
**A:**  
FastAPI requires an ASGI server like Uvicorn to handle incoming web requests.

---

### Explanation
- FastAPI is a framework, not a server
- Uvicorn provides the runtime environment
- It supports asynchronous request handling
- It is lightweight and fast

Without Uvicorn, the FastAPI application cannot be accessed through a browser or API client.

---

### One-line viva answer
> “Uvicorn is required because FastAPI needs an ASGI server to handle HTTP requests.”

---

## Q: Why is Uvicorn listed inside `requirements.txt`?
**A:**  
Uvicorn is listed because it is required to run the backend application.

---

### Explanation
- The backend depends on Uvicorn at runtime
- Listing it ensures it is installed along with FastAPI
- This avoids manual installation steps
- It simplifies setup on new systems

---

### One-line viva answer
> “Uvicorn is included because it is required to run the FastAPI backend.”

---

## Q: How do `requirements.txt` and Uvicorn work together in this project?
**A:**  
`requirements.txt` installs Uvicorn, and Uvicorn runs the FastAPI backend.

---

### Explanation
- `requirements.txt` defines dependencies
- `pip install -r requirements.txt` installs them
- Uvicorn starts the backend server
- FastAPI handles API logic on top of it

This separation keeps the backend clean and modular.

---

### One-line viva answer
> “`requirements.txt` installs Uvicorn, and Uvicorn runs the FastAPI application.”

## Q: What is WSGI?
**A:**  
WSGI (Web Server Gateway Interface) is a standard interface that allows Python web applications to communicate with web servers.

---

### Explanation
- WSGI defines how a web server forwards HTTP requests to a Python application
- It is designed for **synchronous** request handling
- Each request is processed one at a time per worker
- It has been traditionally used by frameworks like Django and Flask

WSGI works well for traditional web applications but is limited for modern, high-concurrency use cases.

---

### One-line viva answer
> “WSGI is a standard interface for running synchronous Python web applications.”

---

## Q: What are the limitations of WSGI?
**A:**  
WSGI does not support asynchronous request handling.

---

### Explanation
- WSGI blocks a worker while processing a request
- It cannot efficiently handle long-running or concurrent tasks
- Real-time or high-frequency APIs perform poorly under WSGI
- Scaling requires spawning more worker processes

These limitations make WSGI less suitable for modern API-based applications.

---

### One-line viva answer
> “WSGI is limited because it only supports synchronous request handling.”

---

## Q: What is ASGI?
**A:**  
ASGI (Asynchronous Server Gateway Interface) is a modern interface standard for Python web applications that supports asynchronous communication.

---

### Explanation
- ASGI extends WSGI to support **asynchronous** execution
- It allows handling multiple requests concurrently
- It supports long-lived connections
- It is designed for modern web APIs

Frameworks like FastAPI are built on ASGI.

---

### One-line viva answer
> “ASGI is a modern interface that supports asynchronous Python web applications.”

---

## Q: Why is ASGI better suited for FastAPI?
**A:**  
FastAPI is designed to handle asynchronous requests efficiently, which requires ASGI.

---

### Explanation
- FastAPI supports async and non-blocking endpoints
- ASGI allows concurrent request handling
- It improves performance for frequent API calls
- It scales better than synchronous models

This makes ASGI ideal for APIs that are called repeatedly, such as system monitoring endpoints.

---

### One-line viva answer
> “FastAPI uses ASGI because it supports asynchronous and concurrent request handling.”

---

## Q: What is the role of Uvicorn in ASGI-based applications?
**A:**  
Uvicorn is an ASGI server that runs ASGI-compatible Python applications.

---

### Explanation
- ASGI defines the interface, not the server
- Uvicorn implements the ASGI protocol
- It listens for HTTP requests and passes them to FastAPI
- It handles concurrency and async execution

Without Uvicorn, an ASGI application cannot serve requests.

---

### One-line viva answer
> “Uvicorn is the ASGI server that runs FastAPI applications.”

---

## Q: How is ASGI different from WSGI?
**A:**  
ASGI supports asynchronous and concurrent request handling, while WSGI supports only synchronous handling.

---

### Explanation
- WSGI processes one request per worker at a time
- ASGI can process multiple requests concurrently
- ASGI is suitable for modern APIs and real-time systems
- WSGI is suited for traditional web applications

---

### One-line viva answer
> “ASGI supports async and concurrency, whereas WSGI is synchronous.”

---

## Q: Why is ASGI important for this project?
**A:**  
ASGI allows efficient handling of frequent API requests for system monitoring.

---

### Explanation
- The frontend polls the backend repeatedly
- ASGI handles multiple polling requests efficiently
- It prevents blocking behavior
- It ensures better responsiveness

This makes the backend scalable and reliable.

---

### One-line viva answer
> “ASGI ensures efficient handling of repeated monitoring requests.”

## Q: Does Uvicorn act as a server in this project?
**A:**  
Yes, Uvicorn acts as the web server that runs the FastAPI application.

---

### Explanation
- FastAPI is a web framework, not a server
- Uvicorn is responsible for listening on a network port
- It accepts incoming HTTP requests from clients
- It forwards these requests to the FastAPI application
- It sends responses back to the client

Without Uvicorn, the FastAPI application cannot be accessed through a browser or API client.

---

### Important distinction
- FastAPI → defines how requests are handled
- Uvicorn → handles network communication and request delivery

Both are required for the backend to function.

---

### One-line viva answer
> “Yes, Uvicorn acts as the web server that runs the FastAPI application.”

## Q: What are the roles and responsibilities of a server in a web application?
**A:**  
A server is responsible for receiving client requests, forwarding them to the application logic, and sending responses back to the client.

---

### Explanation
A web server performs the following core responsibilities:
- Listens on a network port (e.g., 8000 or 80)
- Accepts incoming HTTP requests from clients
- Passes requests to the application framework
- Manages concurrent connections
- Sends HTTP responses back to clients

The server does not contain business logic; it only manages communication.

---

### One-line viva answer
> “A server handles network communication and request–response delivery.”

---

## Q: How does Uvicorn fulfill the role of a server when used with FastAPI?
**A:**  
Uvicorn fulfills the server role by acting as an ASGI-compliant web server for FastAPI.

---

### Explanation
- Uvicorn listens for incoming HTTP requests
- It implements the ASGI protocol
- It forwards requests to FastAPI endpoint functions
- It manages concurrency and asynchronous execution
- It sends FastAPI responses back to the client

FastAPI handles application logic, while Uvicorn handles communication.

---

### One-line viva answer
> “Uvicorn runs the FastAPI application and handles HTTP communication.”

---

## Q: Why is Uvicorn required when using FastAPI?
**A:**  
FastAPI requires an ASGI server like Uvicorn to receive and process web requests.

---

### Explanation
- FastAPI is a framework, not a server
- It defines how requests should be handled
- Uvicorn provides the runtime environment
- Without Uvicorn, FastAPI cannot listen on a network port

Thus, Uvicorn is mandatory to make FastAPI accessible.

---

### One-line viva answer
> “FastAPI needs Uvicorn because it does not include a built-in server.”

---

## Q: Why don’t we explicitly use Uvicorn-like servers in Flask or Django?
**A:**  
Flask and Django traditionally run on WSGI servers that are often hidden from the developer.

---

### Explanation
- Flask and Django are WSGI-based frameworks
- They are commonly run using servers like Gunicorn or uWSGI
- During development, Flask and Django provide built-in development servers
- These built-in servers hide the underlying WSGI server concept

In contrast, FastAPI explicitly uses an ASGI server like Uvicorn.

---

### One-line viva answer
> “Flask and Django hide the server layer, while FastAPI requires an explicit ASGI server.”

---

## Q: What is the difference between how FastAPI and Flask/Django are served?
**A:**  
FastAPI is served using an ASGI server, while Flask and Django are traditionally served using WSGI servers.

---

### Explanation
- FastAPI → ASGI → Uvicorn
- Flask/Django → WSGI → Gunicorn/uWSGI
- ASGI supports asynchronous execution
- WSGI supports synchronous execution

This architectural difference explains why Uvicorn is explicitly used with FastAPI.

---

### One-line viva answer
> “FastAPI uses ASGI servers like Uvicorn, while Flask and Django use WSGI servers.”

---

## Q: Is Uvicorn only used in development?
**A:**  
No, Uvicorn can be used in both development and production environments.

---

### Explanation
- Uvicorn is lightweight and production-capable
- It can be run directly or behind a process manager
- It supports high concurrency and async workloads
- It is commonly used in real-world FastAPI deployments

---

### One-line viva answer
> “Uvicorn can be used in both development and production.”

---

## Q: Why does the FastAPI backend execute the C++ binary instead of reimplementing monitoring in Python?

**A:**
The monitoring logic is already implemented in C++ because the project focuses on low-level system programming.

Instead of rewriting the logic in Python, the backend executes the compiled binary and reads its JSON output.

This allows the project to maintain a clear separation between system-level logic and web API functionality.

### One-line viva answer

> “The FastAPI backend executes the C++ engine to preserve low-level monitoring logic.”

---

## Q: Why does the C++ engine return JSON output?

**A:**
JSON is a standard data exchange format used by web APIs.

Returning JSON allows the backend to easily parse the system statistics and send them to the frontend.

This simplifies communication between the system engine, backend server, and web client.

### One-line viva answer

> “JSON is used because it is the standard format for API data exchange.”

---

## Q: Why is `requirements.txt` used in the backend?

**A:**
The `requirements.txt` file lists all Python dependencies required by the backend.

This allows dependencies to be installed automatically using `pip`.

It ensures that the backend runs consistently across different environments.

### One-line viva answer

> “`requirements.txt` ensures consistent installation of backend dependencies.”

---

# File: `docs/viva/linux_procfs.md`

---

## Q: Why are `/proc/stat` and `/proc/meminfo` used for monitoring?

**A:**
The Linux `/proc` filesystem exposes real-time kernel information about system resources.

The project reads:

* `/proc/stat` to calculate CPU usage
* `/proc/meminfo` to calculate memory usage

These files provide direct access to kernel-level statistics.

### One-line viva answer

> “`/proc/stat` and `/proc/meminfo` provide real-time CPU and memory statistics.”

---