# 🏠 Day 53 – Data Entry Automation

> Automating the process of collecting property data from Zillow and entering it into a Google Form using Python, BeautifulSoup, and Selenium.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green?style=for-the-badge)
![Selenium](https://img.shields.io/badge/Selenium-Automation-orange?style=for-the-badge)

---

## 📌 Project Overview

In this project, I built a **data entry automation bot** that:

1. Scrapes rental property information from a Zillow webpage.
2. Extracts:

   * 🏠 Property addresses
   * 💰 Rental prices
   * 🔗 Property listing URLs
3. Opens a Google Form using Selenium.
4. Automatically enters the collected information into the form.
5. Submits the form for each property.

The goal of this project is to combine **web scraping** with **browser automation** to eliminate repetitive manual data entry.

---

## 🛠️ Technologies Used

* **Python**
* **BeautifulSoup** – for parsing HTML and extracting property data
* **Requests** – for retrieving webpage content
* **Selenium WebDriver** – for browser automation
* **Google Forms** – as the destination for the scraped data

---

## 🔎 Data Extraction

BeautifulSoup is used to locate the property addresses:

```python
addresses = soup.find_all(
    "address",
    attrs={"data-test": "property-card-addr"}
)

for address in addresses:
    print(address.get_text(strip=True))
```

Rental prices are extracted from the property price elements:

```python
prices = soup.find_all(
    "span",
    attrs={"data-test": "property-card-price"}
)
```

A regular expression is used to keep only the actual price:

```python
import re

for price in prices:
    price_text = price.get_text(strip=True)
    price_only = re.search(r"\$[\d,]+", price_text).group()
    print(price_only)
```

This converts values such as:

```text
$2,895+/mo
$2,798+ 1bd
$2,450/mo
```

into:

```text
$2,895
$2,798
$2,450
```

Property links are extracted from the `href` attribute:

```python
links = [
    link.get("href")
    for link in soup.find_all(
        "a",
        attrs={"data-test": "property-card-link"}
    )
]
```

---

## 🤖 Selenium Automation

Selenium is used to open the Google Form and interact with its input fields.

The project uses `WebDriverWait` and expected conditions to wait for elements before interacting with them:

```python
link = wait.until(
    ec.element_to_be_clickable(
        (By.CSS_SELECTOR, "input.whsOnd")
    )
)
```

For multiple Google Form inputs, the elements can be collected using:

```python
inputs = driver.find_elements(
    By.CSS_SELECTOR,
    "input.whsOnd"
)
```

Individual fields can then be accessed using their index:

```python
inputs[0]
inputs[1]
inputs[2]
```

---

## 🔄 Project Workflow

```text
Zillow
   ↓
Requests
   ↓
BeautifulSoup
   ↓
Extract Addresses + Prices + Links
   ↓
Selenium
   ↓
Google Form
   ↓
Automatically Fill Form
   ↓
Submit
```

---

## 📚 What I Learned

### BeautifulSoup

* Finding elements with `find_all()`
* Using HTML attributes to locate specific elements
* Extracting clean text with `.get_text(strip=True)`
* Extracting attributes with `.get()`
* Combining BeautifulSoup with regular expressions

### Regular Expressions

I learned how to extract only the required part of a string using:

```python
re.search(r"\$[\d,]+", price_text).group()
```

### Selenium

* Finding elements using CSS selectors
* Using `find_element()` and `find_elements()`
* Using `.send_keys()` to enter text
* Using `.click()` to interact with buttons
* Using `WebDriverWait`
* Using `element_to_be_clickable()`
* Working with multiple elements and indexes

---

## 💡 Key Concept

One important lesson from this project was the difference between:

```python
"input.whsOnd"[1]
```

and:

```python
driver.find_elements(
    By.CSS_SELECTOR,
    "input.whsOnd"
)[1]
```

The first attempts to index the **Python string**, while the second selects the **second WebElement** returned by Selenium.

---

## 🚀 Future Improvements

Possible improvements include:

* Automatically handling multiple pages of listings
* Adding error handling for missing property information
* Storing the scraped data in a CSV file before submission
* Making the Google Form selectors more robust
* Adding logging for successful and failed submissions

---

## 📁 Project Structure

```text
Day-53-Data-Entry-Automation/
│
├── main.py
└── README.md
```

---

## 🎯 Day 53 Completed

**Day 53 of 100 Days of Python completed!**

This project combined **web scraping, regular expressions, and Selenium browser automation** to create an automated data-entry workflow.
