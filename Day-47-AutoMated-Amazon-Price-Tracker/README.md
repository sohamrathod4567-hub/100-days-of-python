# Day 47 – Automated Amazon Price Tracker

## Overview

This project is an **Automated Amazon Price Tracker** built with Python.

The program checks the current price of a product from a webpage and compares it with a target price. If the product price falls below the target price, the program automatically sends an email notification using Gmail SMTP.

This project combines **web scraping, environment variables, conditional logic, and automated email notifications**.

## Concepts Practiced

* Web scraping with `requests`
* Parsing HTML with `BeautifulSoup`
* Extracting product prices from HTML
* String manipulation
* Type conversion using `float()`
* Conditional statements
* Sending emails with `smtplib`
* Gmail SMTP and STARTTLS
* Using environment variables with `python-dotenv`
* Protecting sensitive credentials
* Using `os.getenv()`
* Working with external libraries

## How to Run

### 1. Install the required libraries

```bash
pip install requests beautifulsoup4 python-dotenv
```

### 2. Create a `.env` file

Store your email credentials in environment variables instead of writing them directly in the Python file.

```env
USERNAME=your_email@gmail.com
G_PASSWORD=your_google_app_password
```

> Use a Google App Password for Gmail authentication rather than your regular Gmail password.

### 3. Run the program

```bash
python main.py
```

The program will:

1. Request the product webpage.
2. Parse the HTML using BeautifulSoup.
3. Extract the product price.
4. Compare it with the target price.
5. Send an email if the price is below the target.

## Example

If the target price is:

```python
TARGET_PRICE = 100
```

and the scraped product price is:

```text
99.0
```

The condition:

```python
if price < TARGET_PRICE:
```

will be true, and the program will send a price-drop alert.

Example output:

```text
99.0
Mail sent!!
```

## What I Learned

* How to scrape information from a webpage using `requests` and `BeautifulSoup`.
* How to extract and clean price information from HTML.
* How to compare scraped data with a predefined target.
* How to send automated emails using Python's `smtplib`.
* How Gmail SMTP works with port `587` and STARTTLS.
* How to use `.env` files to keep credentials outside the source code.
* How multiple Python libraries can be combined to create an automated application.

## Project Status

**Completed**

The project successfully demonstrates an automated workflow that monitors a product price and sends an email notification when the price drops below the desired target.
