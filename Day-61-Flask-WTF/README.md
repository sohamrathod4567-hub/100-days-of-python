# Day 61 - Flask-WTF & Bootstrap-Flask Login Form

## Overview

In Day 61 of the 100 Days of Python Bootcamp, I continued working with Flask and created a login form using **Flask-WTF** and **Bootstrap-Flask**.

The project focuses on creating and rendering forms in Flask while using Bootstrap to automatically style the form and improve the user interface.

## Concepts Practiced

* Flask
* Flask-WTF
* WTForms
* Bootstrap-Flask
* Bootstrap 5
* Flask templates
* Jinja2
* Template inheritance
* `render_form()`
* Form rendering
* HTML forms
* Form validation
* Python virtual environments

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project directory:

```bash
cd Day-61
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

4. Install the required packages:

```bash
pip install flask flask-wtf bootstrap-flask
```

5. Run the Flask application:

```bash
python main.py
```

6. Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## Example

The login page uses Bootstrap-Flask's `render_form()` function to automatically generate a Bootstrap-styled form.

```html
{% extends "base.html" %}
{% from 'bootstrap5/form.html' import render_form %}

{% block title %}Login{% endblock %}

{% block content %}
    <div class="container">
        <h1>Login</h1>
        {{ render_form(form) }}
    </div>
{% endblock %}
```

## What I Learned

* How to create forms using Flask-WTF.
* How WTForms can simplify form creation and validation.
* How to integrate Bootstrap 5 into a Flask application using Bootstrap-Flask.
* How to use `render_form()` to generate styled forms automatically.
* How Flask template inheritance works with `base.html`.
* How Jinja2 blocks can be used to structure reusable templates.

## Project Status

Completed as part of the **100 Days of Python Bootcamp**.

**Day 61: Flask-WTF & Bootstrap-Flask**
