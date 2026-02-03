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
