# Day 59 – Blog Capstone Project

## Overview

Day 59 of the 100 Days of Python Bootcamp focused on building a complete Blog Capstone Project using Flask.

The project combines Flask, Jinja2 templates, HTML, CSS, Bootstrap, and APIs to create a dynamic blog website where blog posts can be displayed and individual posts can be viewed.

## Concepts Practiced

* Flask
* Jinja2 Templates
* Template Inheritance
* Flask Routes
* Dynamic URL Routing
* GET Requests
* API Integration
* JSON Data
* render_template()
* Passing data from Flask to HTML
* Jinja2 for loops
* Jinja2 variables
* Bootstrap
* HTML & CSS
* Static Files
* Dynamic Blog Pages

## Project Features

* Home page displaying multiple blog posts
* Dynamic blog post pages
* Individual post URLs
* Blog post data retrieved from an API
* Jinja2 used to dynamically generate HTML
* Reusable HTML templates
* Responsive design using Bootstrap
* Navigation between blog pages

## Project Structure

Day-59/
├── main.py
├── templates/
│   ├── index.html
│   ├── post.html
│   └── header.html
└── static/
└── css/
└── styles.css

## How to Run

1. Make sure Python is installed.

2. Install Flask:

pip install flask

3. Navigate to the project directory:

cd Day-59

4. Run the Flask application:

python main.py

5. Open the local development server in your browser:

http://127.0.0.1:5000/

## Example

The home page displays available blog posts.

Clicking on a post takes the user to a dynamic URL such as:

/post/1

The Flask application retrieves the corresponding post and renders it using a Jinja2 template.

## What I Learned

Through this project, I learned how to build a dynamic website using Flask and connect backend Python code with frontend HTML templates.

I also practiced working with APIs and JSON data, creating dynamic routes, passing information between Flask and Jinja2 templates, and organizing a Flask project using templates and static files.

## Project Status

Completed as part of the 100 Days of Python Bootcamp – Day 59.
