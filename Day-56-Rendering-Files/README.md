# Day 56 – Rendering HTML Files with Flask

## Overview

Day 56 of my 100 Days of Python journey focuses on rendering HTML files using Flask and Jinja2.

In this project, I learned how to connect a Python Flask application with an HTML template and display the HTML page in a web browser.

## What I Learned

- Creating a Flask web application
- Using `render_template()`
- Rendering HTML files with Flask
- Understanding the `templates` folder
- Connecting Python backend with HTML frontend
- Using Flask routes
- Running a Flask development server
- Understanding the basics of Jinja2

## Technologies Used

- Python
- Flask
- Jinja2
- HTML
- Git & GitHub

## Project Structure

Day-56-Rendering-Files/
├── templates/
│   └── index.html
├── server.py
└── README.md

## How It Works

Flask automatically looks for HTML files inside a folder named `templates`.

The Flask application uses `render_template()` to load and display the HTML file.

Example:

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

When a user visits the home route, Flask renders the `index.html` file from the `templates` folder.

## Running the Project

### 1. Activate the virtual environment

On Windows PowerShell:

.venv\Scripts\Activate.ps1

### 2. Run the Flask application

python server.py

### 3. Open the application

Open the following address in your browser:

http://127.0.0.1:5000/

## Important Concept – render_template()

Instead of writing HTML directly inside Python:

return "<h1>Hello World</h1>"

we can keep our HTML in a separate file:

return render_template("index.html")

This makes the project cleaner and separates the backend Python code from the frontend HTML.

## Request Flow

Browser
    ↓
Flask Route
    ↓
Python Function
    ↓
render_template()
    ↓
templates/index.html
    ↓
HTML displayed in Browser

## Key Takeaway

The main goal of this project was to understand how Flask renders HTML templates using Jinja2.

The `templates` folder is important because Flask automatically searches this folder when `render_template()` is used.

## Learning Progress

- [x] Flask application
- [x] Flask routes
- [x] HTML templates
- [x] render_template()
- [x] Templates folder
- [x] Connecting backend with frontend
- [x] Running Flask in debug mode
- [x] Basic Jinja2 concepts

## 100 Days of Python

Day 56 / 100

Continuing to improve my Python, Flask, web development, automation, and backend development skills through the 100 Days of Code – Python challenge.