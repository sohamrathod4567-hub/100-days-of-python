# Day 32 - Email Automation with SMTP 📧

## Overview

On **Day 32** of the **100 Days of Python** challenge, I learned how to automate email sending using Python's built-in `smtplib` module. I explored the **Simple Mail Transfer Protocol (SMTP)**, securely logged into a Gmail account using an App Password, and sent emails directly from a Python script.

I also learned how to work with the `datetime` module to create a program that performs actions based on the current day of the week, laying the foundation for scheduling and automation projects.

---

## Concepts Practiced

* Sending emails with Python
* Understanding the SMTP protocol
* Using the `smtplib` library
* Secure email authentication with Gmail App Passwords
* Creating secure connections using `starttls()`
* Working with the `datetime` module
* Retrieving the current date and time
* Determining the current weekday
* Automating tasks based on specific days
* Using context managers (`with` statement)
* Writing cleaner and more secure Python code

---

## Project Features

* 📧 Send emails automatically using Gmail SMTP
* 🔐 Secure login with Gmail App Passwords
* 📅 Detect the current day using the `datetime` module
* 🤖 Perform actions only on selected days
* 🐍 Practice working with Python's built-in libraries

---

## Technologies Used

* Python 3
* `smtplib`
* `datetime`

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

2. Navigate to the project folder.

```bash
cd Day-32-Email_SMTP
```

3. Add your Gmail credentials.

```python
MY_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

> **Note:** Use a Gmail **App Password** instead of your normal account password.

4. Run the program.

```bash
python main.py
```

---

## Example Output

```
Email sent successfully!
```

Or, if scheduled for a particular day:

```
Today is Wednesday.
Sending motivational email...
Email sent successfully!
```

---

## What I Learned

* How email communication works using SMTP.
* The difference between SMTP ports (587 with TLS and 465 with SSL).
* How to securely authenticate with Gmail using App Passwords.
* How to establish encrypted email connections using `starttls()`.
* How to use Python's `datetime` module to retrieve the current date and weekday.
* How automation can be built by combining email functionality with date-based logic.
* Best practices for handling credentials securely.

---

## Project Status

✅ Completed

This project marks my introduction to **email automation** in Python and serves as the foundation for future automation projects such as birthday reminders, scheduled notifications, and personalized email campaigns.

---

## Author

**Soham Rathod**

Building one project every day as part of the **100 Days of Python** challenge.
