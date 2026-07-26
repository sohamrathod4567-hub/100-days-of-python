# Day 30 – Password Manager 🗝️

## Overview

On Day 30 of the **100 Days of Python** challenge, I enhanced the Password Manager application by implementing **exception handling** and **JSON-based data storage**. The application now allows users to securely save, search, and manage website credentials while gracefully handling errors such as missing files or websites.

This project focuses on making applications more robust and user-friendly by preventing crashes and preserving existing data.

---

## Concepts Practiced

- Exception Handling (`try`, `except`, `else`, `finally`)
- Raising Exceptions
- `FileNotFoundError`
- `KeyError`
- JSON file handling
- Reading and writing JSON files
- Updating dictionaries
- Data persistence
- Tkinter GUI development
- Input validation

---

## Features

- 🔐 Generate secure random passwords
- 💾 Save website credentials locally in a JSON file
- 🔍 Search for saved website credentials
- 📋 Automatically copy generated passwords to the clipboard
- ⚠️ Handle missing files without crashing
- ❌ Notify users when a website is not found
- ✏️ Update existing data without overwriting previous entries
- ✅ Validate user input before saving

---

## Project Structure

```
Day-30/
│── main.py
│── logo.png
│── data.json
└── README.md
```

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

2. Navigate to the project folder:

```bash
cd Day-30
```

3. Install the required package:

```bash
pip install pyperclip
```

4. Run the application:

```bash
python main.py
```

---

## Example

When saving credentials:

```text
Website : github.com
Email   : soham@example.com
Password: x7@Qm91#Lp
```

Searching for a website:

```text
Website: github.com

Email: soham@example.com
Password: x7@Qm91#Lp
```

---

## What I Learned

- How to use Python's exception handling to build reliable applications.
- The difference between `try`, `except`, `else`, and `finally`.
- How to work with JSON files for storing structured data.
- How to update JSON data while preserving existing records.
- How to handle missing files and missing dictionary keys.
- The importance of validating user input before processing it.
- How to improve the user experience by displaying meaningful error messages.

---

## Future Improvements

- Encrypt stored passwords for better security.
- Add functionality to edit existing credentials.
- Allow deletion of saved websites.
- Add password strength indicators.
- Store credentials in a database instead of a JSON file.
- Implement a master password for application access.

---

## Project Status

✅ Completed

---

### Part of

This project is part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

**Day 30:** Password Manager with Exception Handling & JSON Storage