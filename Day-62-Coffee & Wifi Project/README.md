# Day 62 – Cafe & WiFi Website

## Overview

Built a Flask web application that allows users to view a list of cafes and add new cafes to a CSV database.

The project uses **Flask-WTF** to create and validate forms, **Bootstrap-Flask** to style the forms, and Python's built-in `csv` module to read and write cafe data.

## Concepts Practiced

* Flask
* Flask routing
* GET and POST requests
* Flask-WTF
* WTForms
* Form validation
* Bootstrap-Flask
* Jinja2 templating
* Template inheritance
* `url_for()`
* Reading CSV files
* Writing to CSV files
* Appending data to CSV files
* `redirect()`
* HTML tables
* Dynamic table generation with Jinja loops
* Environment configuration with `SECRET_KEY`

## Features

* View all cafes stored in the CSV file
* Add a new cafe through a web form
* Validate form fields
* Select coffee, WiFi, and power ratings
* Store new cafe information in `cafe-data.csv`
* Dynamically display cafe information in a Bootstrap table
* Open cafe locations through Google Maps links

## Project Structure

```text
Day-62-Cafe-Wifi/
│
├── main.py
├── cafe-data.csv
├── requirements.txt
│
├── static/
│   └── css/
│       └── styles.css
│
└── templates/
    ├── base.html
    ├── index.html
    ├── add.html
    └── cafes.html
```

## How to Run

1. Clone or download the project.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python main.py
```

4. Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Example

A cafe entry contains:

```text
Cafe Name: Lighthaus
Location: Google Maps link
Opening Time: 11AM
Closing Time: 3:30PM
Coffee: ☕☕☕☕
WiFi: ✘✘
Power: 🔌🔌🔌
```

The information is saved as a new row in:

```text
cafe-data.csv
```

## What I Learned

This project helped me understand how Flask applications can work with forms and external data files.

I learned how to:

* Create forms using Flask-WTF
* Validate user input
* Handle GET and POST requests
* Use Bootstrap-Flask to render styled forms
* Read CSV data and pass it to Jinja templates
* Dynamically generate HTML tables using Jinja
* Write submitted form data to a CSV file
* Redirect users after successfully submitting a form
* Use `url_for()` for dynamic Flask URLs

## Project Status

Completed
