# Day 48 – Selenium Web Driver

## Overview

Day 48 of the **100 Days of Code – The Complete Python Pro Bootcamp** focused on **Selenium WebDriver and browser automation**.

In this project, I learned how to use Selenium to control a web browser with Python. I practiced finding HTML elements, interacting with webpages, clicking buttons, entering text, and automating browser-based tasks.

The main project was a **Cookie Clicker automation bot** that uses Selenium to interact with the Cookie Clicker game.

## Concepts Practiced

- Selenium WebDriver
- Launching and controlling Chrome
- Opening webpages with Selenium
- Finding HTML elements using:
  - `By.ID`
  - `By.NAME`
  - `By.CLASS_NAME`
  - `By.CSS_SELECTOR`
- Clicking buttons and elements
- Entering text into input fields
- Reading text from webpages
- Browser automation
- Working with dynamically loaded webpages
- Using `time.sleep()`
- Understanding `NoSuchElementException`
- Debugging Selenium selectors

## How to Run

1. Install Selenium:

    pip install selenium

2. Navigate to the Day 48 folder:

    cd Day-48-selenium-Web-Driver

3. Run the Cookie Clicker project:

    python Cookie-Clicker.py

## Example

Basic Selenium interaction:

    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()

    driver.get("https://orteil.dashnet.org/cookieclicker/")

    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()

Selenium can also interact with form elements:

    element = driver.find_element(By.NAME, "fname")
    element.send_keys("Soham")

## What I Learned

This project taught me how Selenium can automate tasks that require interaction with a real web browser.

I learned how to:

- Open and control Chrome using Python.
- Locate elements on webpages.
- Interact with buttons, forms, and other elements.
- Automate repetitive browser tasks.
- Debug Selenium element-selection errors.
- Understand why website changes can break Selenium selectors.
- Use Selenium for real-world browser automation.

## Project Status

**Completed**

Day 48 of the **100 Days of Code – The Complete Python Pro Bootcamp**.