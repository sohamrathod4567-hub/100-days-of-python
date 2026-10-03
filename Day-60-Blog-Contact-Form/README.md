# Day 60 - Flask Blog Contact Form

## Overview

On Day 60 of the 100 Days of Python challenge, I built a Blog Website with a Contact Form using Flask.

The project demonstrates how to handle HTML forms in Flask, receive user-submitted data, process POST requests, and send the submitted information through email using Python's smtplib module.

## Concepts Practiced

- Flask
- Flask Routing
- GET and POST Requests
- HTML Forms
- Handling Form Data with request.form
- Jinja2 Templates
- render_template()
- redirect()
- Python smtplib
- Gmail SMTP
- Sending Emails with Python
- Bootstrap
- Static Files
- Environment Variables
- Flask Debugging

## Project Structure

Day-60-Blog-Contact-Form/
│
├── main.py
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── ...
│
├── static/
│   ├── css/
│   │   └── styles.css
│   │
│   ├── js/
│   │   └── scripts.js
│   │
│   └── assets/
│       └── img/
│
└── README.md

## How It Works

The website contains a contact page where users can enter their:

- Name
- Email
- Phone Number
- Message

When the user submits the form, Flask receives the information through a POST request.

Example:

    data = request.form

    send_email(
        data["name"],
        data["email"],
        data["phone"],
        data["message"]
    )

The send_email() function then uses Gmail's SMTP server to send the submitted information by email.

## Email Configuration

The project uses Gmail SMTP.

Example:

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)

For Gmail authentication, an App Password should be used instead of the normal Gmail account password.

Sensitive credentials should be stored using environment variables instead of being directly written in the source code.

## How to Run

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment on Windows:

    .venv\Scripts\activate

Install Flask:

    pip install flask

Run the application:

    python main.py

The application will run locally at:

    http://127.0.0.1:5001

## Example

The user visits:

    /contact

The contact form collects information such as:

    Name: John Doe
    Email: john@example.com
    Phone: 1234567890
    Message: I would like to contact you.

Flask receives the submitted form data and passes it to the email function.

## What I Learned

- How Flask handles HTML form submissions.
- How GET and POST requests work.
- How to retrieve submitted form data using request.form.
- How to connect a frontend form with Python backend logic.
- How Python communicates with an SMTP server.
- How to send emails using smtplib.
- Why sensitive credentials should not be hard-coded.
- How to debug Flask applications using the development server.

## Project Status

Completed as part of the 100 Days of Python Bootcamp.

Day: 60

Project: Blog Contact Form

Main Technology: Python + Flask