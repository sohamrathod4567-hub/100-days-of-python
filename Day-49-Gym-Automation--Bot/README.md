# Day 49 – Gym Automation Bot

## Project Overview

This project is a **Gym Class Booking Automation Bot** built with Python and Selenium.

The bot automatically logs into a gym website, checks the available classes, and books a selected class. It can also be used to check class availability for different days.

## What I Learned

* Using **Selenium WebDriver** to automate a website
* Finding elements using Selenium's `By` class
* Using `WebDriverWait` and Expected Conditions
* Handling login forms
* Clicking buttons automatically
* Reading information from web pages
* Working with dynamic web elements
* Automating a real-world browser task

## Technologies Used

* Python
* Selenium
* Chrome WebDriver

## Project Structure

```text
Day-49-Gym-Automation--Bot/
│
├── main.py
└── README.md
```

## How It Works

The automation follows these basic steps:

1. Open the gym website.
2. Log in using the account credentials.
3. Navigate to the gym class booking section.
4. Select the required day.
5. Check the available classes.
6. Find the desired class.
7. Book the class automatically.

## Important Selenium Concepts

### WebDriver

Selenium WebDriver allows Python to control a web browser programmatically.

```python
from selenium import webdriver

driver = webdriver.Chrome()
```

### Finding Elements

Elements can be located using different methods:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "element_id")
driver.find_element(By.NAME, "element_name")
driver.find_element(By.CLASS_NAME, "class_name")
driver.find_element(By.CSS_SELECTOR, "css_selector")
```

### Explicit Waits

Since modern websites often load elements dynamically, `WebDriverWait` can be used instead of immediately searching for an element.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

wait = WebDriverWait(driver, 10)

element = wait.until(
    ec.presence_of_element_located((By.ID, "element_id"))
)
```

This makes the automation more reliable because Selenium waits until the required element is available.

## Credentials

Do **not** store real login credentials directly in your source code.

Instead of:

```python
ACCOUNT_EMAIL = "your_email@example.com"
ACCOUNT_PASSWORD = "your_password"
```

consider using environment variables:

```python
import os

ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
```

This prevents sensitive credentials from accidentally being uploaded to GitHub.

## Key Takeaway

Day 49 focused on using Selenium for a practical automation project. Instead of simply interacting with individual web elements, the project combines **login automation, navigation, waiting for dynamic elements, extracting information, and performing actions** to automate a complete workflow.

This project demonstrates how Python and Selenium can be used to automate repetitive browser-based tasks.
