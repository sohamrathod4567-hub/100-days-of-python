# 🐦 Day 51 – Twitter Complaint Bot

> Day 51 of my **100 Days of Code: The Complete Python Pro Bootcamp** journey by Dr. Angela Yu.

## 📌 Project Overview

For Day 51, I built a **Twitter Complaint Bot** using Python and Selenium.

The bot checks my internet speed and compares the actual download and upload speeds with the speeds promised by my Internet Service Provider (ISP).

If the internet speed is lower than the promised speed, the bot automatically logs into Twitter/X and posts a complaint about the poor internet performance.

## 🚀 Features

- 🌐 Checks internet download speed
- 📤 Checks internet upload speed
- 📊 Compares actual speed with the promised ISP speed
- 🤖 Automates browser actions using Selenium
- 🔐 Logs into Twitter/X automatically
- ✍️ Creates a complaint based on the speed test results
- 🐦 Posts the complaint on Twitter/X

## 🛠️ Technologies Used

- Python 3
- Selenium
- Chrome WebDriver
- Internet Speed Test
- Twitter/X

## 📂 Project Structure

    Day-51-Twitter-Complaint-Bot/
    │
    ├── main.py
    ├── internet_speed_bot.py
    └── README.md

## ⚙️ How It Works

The bot follows this workflow:

    Start
      ↓
    Open Internet Speed Test
      ↓
    Measure Download & Upload Speed
      ↓
    Compare with Promised ISP Speed
      ↓
    Is the Speed Lower?
      ↓
      ├── Yes → Open Twitter/X
      │          ↓
      │        Log In
      │          ↓
      │        Create Complaint
      │          ↓
      │        Post Tweet
      │
      └── No → Finish

## 💻 Example

Suppose my ISP promises:

    Download: 100 Mbps
    Upload: 20 Mbps

But the speed test returns:

    Download: 65 Mbps
    Upload: 12 Mbps

The bot can automatically generate a complaint such as:

    Hey ISP, why am I getting 65 Mbps download and 12 Mbps upload
    when I am paying for 100 Mbps download and 20 Mbps upload?

## 🧠 What I Learned

Through this project, I practiced:

- Using Selenium WebDriver
- Finding elements using Selenium selectors
- Automating buttons, inputs, and forms
- Using explicit waits
- Working with dynamically loaded web pages
- Automating login processes
- Extracting information from websites
- Comparing values programmatically
- Using Object-Oriented Programming (OOP)
- Building a practical browser automation project

## 🔎 Selenium Concepts

One of the important concepts in this project was using explicit waits.

Instead of trying to interact with an element immediately, Selenium can wait until the element is available.

Example:

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

Explicit waits are useful when working with websites where elements take some time to load.

## 🔐 Security Note

Credentials should **never be hard-coded** directly into the source code.

Avoid storing credentials like this:

    ACCOUNT_EMAIL = "myemail@example.com"
    ACCOUNT_PASSWORD = "mypassword"

A safer approach is to use environment variables:

    import os

    ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
    ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")

This prevents sensitive credentials from accidentally being uploaded to GitHub.

## 🎯 Project Goal

The goal of this project was to automate the process of checking internet performance and complaining to the ISP when the actual speed is significantly lower than the promised speed.

The project demonstrates how Python and Selenium can be used to automate a complete real-world workflow:

    Data Collection
          ↓
    Speed Comparison
          ↓
    Problem Detection
          ↓
    Browser Automation
          ↓
    Automated Complaint

## 📚 Key Takeaways

This project helped me understand how Selenium can be used beyond simple web scraping.

I learned how to:

- Automate real websites
- Handle dynamically loaded elements
- Use waits effectively
- Interact with forms and buttons
- Automate login workflows
- Combine multiple automation steps into one application

## 📈 Progress

**Day 51 / 100 Days of Python**

**51% Complete**

> Continuing my journey of learning Python through practical projects and automation.