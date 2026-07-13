# ☕ Day 15 – Coffee Machine

A Python simulation of a coffee vending machine that prepares **Espresso**, **Latte**, and **Cappuccino** while managing available resources, accepting coin payments, calculating change, and generating machine reports.

---

## 📌 Overview

This project simulates the working of a real coffee machine. The user can choose a drink, insert coins, and receive their beverage if enough resources and payment are available. The machine keeps running until it is turned off by the user.

---

## 🧠 Concepts Practiced

- Functions
- Dictionaries
- Nested Dictionaries
- Loops (`while` & `for`)
- Conditional Statements
- Global Variables
- Input Validation
- Resource Management
- Function Parameters
- Boolean Flags
- Floating Point Formatting (`:.2f`)
- Code Refactoring

---

## 🚀 Features

- ☕ Choose between:
  - Espresso
  - Latte
  - Cappuccino
- 💰 Coin payment system
- 💵 Automatic change calculation
- 📊 Machine resource report
- 🥛 Resource availability checking
- 🚫 Handles insufficient resources
- ❌ Handles invalid drink selections
- 🔁 Continuous operation until turned off
- 💲 Tracks total money earned by the machine

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/sohamrathod4567-hub/100-days-of-python.git
```

2. Navigate to the Day 15 folder.

```bash
cd Day-15
```

3. Run the program.

```bash
python main.py
```

---

## 💻 Example

```text
What would you like? (espresso / latte / cappuccino): latte

Please Enter quarters: 10
Please Enter dimes: 0
Please Enter nickles: 0
Please Enter pennies: 0

Your total is: 2.50$

Enjoy your latte
```

### Report Command

```text
What would you like? report

Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.50
```

---

## 📚 What I Learned

While building this project, I learned how to:

- Work with nested dictionaries efficiently.
- Break a larger program into smaller reusable functions.
- Pass arguments between functions instead of relying on global variables.
- Validate user input before processing it.
- Simulate a real-world system using Python.
- Manage resources dynamically by updating dictionary values.
- Calculate payments and return change.
- Format floating-point numbers for currency output.
- Organize code into a cleaner and more maintainable structure.

---

## 📁 Project Structure

```text
Day-15/
│── main.py
└── README.md
```

---

## 🎯 Project Status

✅ Completed

This project is part of the **100 Days of Python Bootcamp** by Dr. Angela Yu.