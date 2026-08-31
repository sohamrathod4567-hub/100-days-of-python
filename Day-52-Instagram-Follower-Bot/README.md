# 🐍 Day 52 - Instagram Follower Bot

> Part of my journey through Dr. Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**.

## 📌 Project Overview

For **Day 52**, I built an **Instagram Follower Bot** using Python and Selenium.

The bot automates the process of finding an Instagram account, opening its followers list, and following users automatically.

This project focuses on using **Selenium WebDriver** to interact with dynamic websites and automate browser actions.

## 🚀 Features

* Opens Instagram using Selenium.
* Logs into an Instagram account.
* Navigates to a target Instagram profile.
* Opens the followers list.
* Finds available **Follow** buttons.
* Automatically clicks Follow buttons.
* Uses Selenium exception handling for intercepted clicks.
* Demonstrates browser automation with dynamic web elements.

## 🛠️ Technologies Used

* **Python 3**
* **Selenium**
* **Chrome WebDriver**
* **HTML/CSS selectors**
* **Exception handling**

## 📂 Project Structure

```text
Day-52-Instagram-Follower-Bot/
│
├── main.py
├── README.md
└── requirements.txt
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

### 2. Navigate to the project

```bash
cd 100-Days-of-Python/Day-52-Instagram-Follower-Bot
```

### 3. Install dependencies

```bash
pip install selenium
```

### 4. Add your Instagram credentials

Update the credentials in `main.py`:

```python
USERNAME = "your_username"
PASSWORD = "your_password"
```

**Do not upload real credentials to GitHub.**

A safer approach is to use environment variables or a `.env` file.

## ▶️ How to Run

Run the following command from the project directory:

```bash
python main.py
```

The bot will open Chrome and perform the configured Instagram actions automatically.

## 🧠 What I Learned

Through this project, I practiced:

* Using Selenium to automate a real website.
* Finding elements using `By.CLASS_NAME`, `By.CSS_SELECTOR`, and other selectors.
* Clicking web elements programmatically.
* Working with dynamically loaded content.
* Handling `ElementClickInterceptedException`.
* Using JavaScript with Selenium when a normal click is intercepted.
* Understanding how browser automation interacts with HTML elements.

## ⚠️ Important Note

This project is intended for **educational purposes** to practice Python and Selenium browser automation.

Automating actions on social-media platforms may violate their terms of service or trigger anti-bot protections. Use automation responsibly and avoid excessive or abusive activity.

## 📚 Course

This project is part of:

**100 Days of Code: The Complete Python Pro Bootcamp**

by **Dr. Angela Yu**

## 👨‍💻 Author

**Soham Rathod**

---

⭐ If you're also learning Python, feel free to explore the other projects in this repository!
