# Day 54 – Flask Introduction

## About

Day 54 focuses on learning the basics of **Flask**, a lightweight Python web framework used to create web applications and APIs.

In this project, I learned how to:

* Create a Flask application.
* Create routes using `@app.route()`.
* Return text from a web page.
* Create multiple URLs/routes.
* Run a Flask development server.
* Use `if __name__ == "__main__":` to start the application.

I also reviewed **Python decorators** and created a simple custom decorator that adds a delay before executing a function.

---

## Technologies Used

* Python
* Flask
* Time module
* Python Decorators

---

## Project Structure

```text
Day-54-Flask/
│
├── main.py
└── README.md
```

---

## Flask Application

The Flask application is created using:

```python
from flask import Flask

app = Flask(__name__)
```

Here, `Flask(__name__)` creates the Flask application.

### Home Route

The `/` route displays **Hello, World!** in the browser:

```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
```

When the Flask server is running, visiting:

```text
http://127.0.0.1:5000/
```

displays:

```text
Hello, World!
```

### Bye Route

A second route was created:

```python
@app.route('/bye')
def say_bye():
    return "Byeee!!!!"
```

Visiting:

```text
http://127.0.0.1:5000/bye
```

displays:

```text
Byeee!!!!
```

---

## Running the Application

First, activate the virtual environment if you are using one.

Then run:

```bash
python main.py
```

Flask will start a local development server.

Open the address shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

---

## Python Decorators

The project also contains a commented-out example of a custom decorator.

```python
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function
```

The decorator adds a **2-second delay** before the decorated function runs.

It can be applied using:

```python
@delay_decorator
def say_hello():
    print("Hello World")
```

This demonstrates how decorators can modify or extend the behavior of existing functions without changing their original code.

---

## What I Learned

### Flask

* Flask is a Python web framework.
* `Flask(__name__)` creates the application.
* `@app.route()` connects a URL to a Python function.
* Flask can return strings directly to the browser.
* `app.run()` starts the development server.

### Decorators

* Decorators are functions that modify the behavior of another function.
* The `@decorator_name` syntax is used to apply a decorator.
* A wrapper function is commonly used inside decorators.

---

## Key Concepts

```text
Python
  │
  ├── Functions
  ├── Decorators
  │
  └── Flask
       │
       ├── Application
       ├── Routes
       ├── Views
       └── Development Server
```

---

## Conclusion

Day 54 introduced me to the fundamentals of **Flask web development** and helped me understand how Python functions can be connected to browser URLs.

I also practiced **Python decorators**, which are an important concept for understanding how Flask and other Python frameworks work.

This project is a starting point for building more advanced Flask applications with HTML, templates, forms, databases, and APIs.
