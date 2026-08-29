# Day 50 – Auto Tinder Swipe Bot

## Project Overview

This project is an **automated Tinder-style swiping bot** built with Python and Selenium.

The project uses Selenium WebDriver to open the Tindog website, interact with the login interface, and automate the process of interacting with profiles.

This project is part of the **100 Days of Code – Python** course.

## What I Learned

* Using Selenium WebDriver for browser automation
* Opening and controlling Chrome with Python
* Finding web elements using different Selenium locators
* Using `WebDriverWait` for dynamic web elements
* Using Expected Conditions
* Clicking buttons automatically
* Interacting with input fields
* Understanding Selenium exceptions
* Debugging `ElementNotInteractableException`
* Debugging `TimeoutException`

## Technologies Used

* Python
* Selenium
* Google Chrome
* Chrome WebDriver

## Project Structure

```text
Day-50-Auto-Tinder-Swipe-Bot/
│
├── main.py
└── README.md
```

## How It Works

The automation follows these basic steps:

1. Start the Chrome browser using Selenium.
2. Open the Tindog website.
3. Locate the login button.
4. Open the login modal.
5. Locate the login options.
6. Interact with the login form.
7. Continue with the automated profile interaction process.

## Selenium Concepts

### Finding Elements

Selenium provides several ways to locate elements:

```python
from selenium.webdriver.common.by import By

driver.find_element(By.ID, "element_id")
driver.find_element(By.NAME, "element_name")
driver.find_element(By.CLASS_NAME, "class_name")
driver.find_element(By.CSS_SELECTOR, "css_selector")
driver.find_element(By.XPATH, "xpath")
```

### Explicit Waits

Web pages do not always load elements immediately. `WebDriverWait` allows Selenium to wait for an element before interacting with it.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

wait = WebDriverWait(driver, 10)

element = wait.until(
    ec.element_to_be_clickable((By.ID, "element_id"))
)
```

### Element to Be Clickable

Instead of immediately clicking an element, Selenium can wait until the element is ready to be interacted with:

```python
element = wait.until(
    ec.element_to_be_clickable((By.XPATH, "your_xpath"))
)

element.click()
```

This is particularly useful for buttons and other interactive elements.

## Errors Encountered

### ElementNotInteractableException

This occurs when Selenium finds an element but the element cannot currently be interacted with.

A common solution is to wait for the element to become clickable:

```python
element = wait.until(
    ec.element_to_be_clickable((By.XPATH, "your_xpath"))
)
```

### TimeoutException

This occurs when Selenium waits for an element but the expected condition is not satisfied within the specified time.

For example:

```python
wait = WebDriverWait(driver, 10)
```

The selector should also be checked to make sure it still matches the current webpage.

## Important Note

Websites can change their HTML structure over time. As a result, Selenium selectors used in older tutorials may stop working.

When this happens, inspect the element using Chrome DevTools and update the Selenium locator accordingly.

## Key Takeaway

Day 50 introduced **browser automation with Selenium** through a Tinder-style swiping project.

The main focus was learning how to locate and interact with dynamic web elements and how to use explicit waits to make Selenium automation more reliable.

This project also provided practical experience with debugging Selenium errors such as `ElementNotInteractableException` and `TimeoutException`.
