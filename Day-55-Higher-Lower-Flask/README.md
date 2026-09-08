# Day 55 – Higher or Lower Game

## Overview

Day 55 of my **100 Days of Python** journey focuses on building a web application using **Flask**.

The project demonstrates how to create a Flask application, define routes, handle requests, and dynamically generate content for a web page.

## What I Learned

* Creating a Flask application
* Using `Flask` and defining routes
* Understanding the `@app.route()` decorator
* Running a Flask development server
* Handling different URLs/endpoints
* Returning HTML content from Flask
* Using Python functions with Flask routes
* Understanding decorators and how Flask uses them

## Technologies Used

* Python
* Flask
* HTML
* Git & GitHub

## Project Structure

```text
Day-55/
│
├── main.py
├── templates/
│   └── index.html
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd Day-55
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Flask

```bash
pip install flask
```

### 5. Run the application

```bash
python main.py
```

The Flask application will start on the local development server.

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Key Concept

One of the main concepts practiced in this project is the Flask route decorator:

```python
@app.route("/")
def home():
    return "Hello World!"
```

The `@app.route()` decorator connects a URL to a Python function. When a user visits that URL, Flask executes the corresponding function and returns its result.

## Learning Progress

* [x] Flask basics
* [x] Routes
* [x] Flask decorators
* [x] Running a local web server
* [x] Returning HTML from Flask
* [ ] Continue building more advanced Flask applications

## 100 Days of Python

**Day 55 / 100**

Continuing to improve my Python, web development, automation, and problem-solving skills through the **100 Days of Code – Python** challenge.
