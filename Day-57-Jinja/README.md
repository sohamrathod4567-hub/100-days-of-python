# Day 57 - Jinja Templating with Flask

## Overview

Day 57 focuses on using **Jinja2 templating with Flask** to create dynamic web pages.

Instead of hardcoding HTML for every page, Jinja allows Python data to be passed from Flask into HTML templates and displayed dynamically.

In this project, blog posts are retrieved from an API and displayed on a homepage. Each blog post has its own page that can be accessed using its unique ID.

---

## What I Learned

* Using **Jinja2** with Flask
* Passing Python variables to HTML templates
* Using `render_template()`
* Using Jinja expressions with `{{ }}`
* Using Jinja loops to display multiple items
* Using Jinja variables inside HTML attributes
* Using Flask dynamic URL parameters
* Using `url_for()` to generate URLs
* Fetching JSON data from an API using `requests`
* Working with dictionaries and lists received from an API
* Creating dynamic blog post pages

---

## Project Structure

```text
Day-57-Jinja/
│
└── project/
    │
    ├── main.py
    │
    └── templates/
        ├── index.html
        └── post.html
```

---

## Flask Application

The Flask application retrieves blog posts from an API and sends them to the Jinja template.

```python
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/ecfe5890e4857ae9911f"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def get_post(id):
    return render_template("post.html", post_id=id)


if __name__ == "__main__":
    app.run(debug=True)
```

---

## Jinja2

Jinja allows Python variables to be inserted into HTML.

For example:

```html
<h1>{{ blog_post['title'] }}</h1>
```

The `{{ }}` syntax tells Jinja to evaluate and display a value.

### Jinja Loop

We can loop through all blog posts:

```html
{% for blog_post in posts %}
    <h1>{{ blog_post['title'] }}</h1>
{% endfor %}
```

Jinja uses:

```text
{% ... %}
```

for statements such as loops and conditions.

It uses:

```text
{{ ... }}
```

for displaying values.

---

## Dynamic URLs

Flask allows us to create dynamic routes:

```python
@app.route('/post/<int:id>')
def get_post(id):
    return render_template("post.html", post_id=id)
```

The `<int:id>` part means Flask expects an integer in the URL.

For example:

```text
/post/1
/post/2
/post/3
```

The ID is passed into the function as the `id` parameter.

---

## Using `url_for()`

Instead of manually creating URLs, Flask's `url_for()` function can generate them.

Example:

```html
<a href="{{ url_for('get_post', id=blog_post['id']) }}">
    Read
</a>
```

If the blog post has an ID of `3`, Flask generates:

```text
/post/3
```

### Important Jinja Rule

Do **not** put another `{{ }}` inside an existing Jinja expression.

Incorrect:

```html
{{ url_for('get_post', id={{ blog_post['id'] }}) }}
```

Correct:

```html
{{ url_for('get_post', id=blog_post['id']) }}
```

---

## Getting Data from an API

The project uses the `requests` library to retrieve blog data:

```python
response = requests.get(blog_url)
```

The JSON response can then be converted into Python data:

```python
all_posts = response.json()
```

The resulting data can be passed to the template:

```python
return render_template("index.html", posts=all_posts)
```

Jinja can then access the data inside `index.html`.

---

## Main Concepts

### Flask

```python
render_template("index.html", posts=all_posts)
```

Passes Python data into an HTML template.

### Jinja

```html
{{ posts }}
```

Displays a variable.

### Jinja Loop

```html
{% for post in posts %}
    ...
{% endfor %}
```

Loops through a collection.

### Flask Dynamic Route

```python
@app.route('/post/<int:id>')
```

Creates a URL containing a dynamic integer.

### URL Generation

```html
{{ url_for('get_post', id=blog_post['id']) }}
```

Creates the correct URL for the Flask route.

---

## How the Application Works

```text
API
 │
 │ JSON data
 ▼
Flask
 │
 │ posts=all_posts
 ▼
index.html
 │
 │ User clicks "Read"
 ▼
/post/<id>
 │
 ▼
get_post(id)
 │
 ▼
post.html
```

---

## Requirements

Install Flask and Requests:

```bash
pip install flask requests
```

Or, if using a virtual environment:

```bash
pip install -r requirements.txt
```

---

## Running the Project

From the project directory:

```bash
python main.py
```

Then open:

```text
http://127.0.0.1:5000/
```

---

## Key Takeaways

Day 57 helped me understand how **Flask and Jinja work together**.

The main idea is:

```text
Python → Flask → Jinja → HTML → Browser
```

Flask handles the application logic and data, while Jinja dynamically inserts that data into HTML templates.

This makes it possible to build dynamic websites without writing separate HTML pages for every piece of content.

---

## Technologies Used

* Python
* Flask
* Jinja2
* Requests
* HTML
* REST API
* JSON

---

## Day 57 Completed

**Topic:** Jinja Templating with Flask

**Project:** Dynamic Blog Website
