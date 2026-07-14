# ☕ Day 16 - Coffee Machine (Object-Oriented Programming)

## 📖 Overview

Welcome to **Day 16** of my **100 Days of Python** challenge!

Today's project is a refactored version of the **Coffee Machine** from Day 15. Instead of writing everything in a single file using procedural programming, I rebuilt the project using **Object-Oriented Programming (OOP)**.

This project simulates a coffee machine that can prepare different drinks, process coins, check available resources, and generate reports—all by utilizing classes and objects for cleaner, more maintainable code.

---

## 🧠 Concepts Practiced

- Object-Oriented Programming (OOP)
- Creating and using classes
- Creating objects from classes
- Object interaction
- Importing custom Python modules
- Encapsulation
- Method calling
- Working with attributes
- Code organization and modularity

---

## 🚀 Features

- ☕ Order Espresso, Latte, or Cappuccino
- 💰 Coin-based payment system
- 📦 Automatically checks available resources
- ✅ Processes successful transactions
- 💵 Returns change when needed
- 📊 Displays a resource and profit report
- 🔌 Turn the machine off using a command
- 🏗️ Organized using multiple classes instead of one large program

---

## 📂 Project Structure

```text
Day-16/
│── main.py
│── menu.py
│── coffee_maker.py
│── money_machine.py
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/100-days-of-python.git
```

2. Navigate to the project folder

```bash
cd Day-16
```

3. Run the program

```bash
python main.py
```

---

## 💻 Example

```text
What would you like? (espresso/latte/cappuccino): latte

Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0

Here is $0.50 in change.
Here is your latte ☕️ Enjoy!
```

---

## 📚 What I Learned

- How Object-Oriented Programming makes code easier to manage.
- How to divide a project into multiple Python files.
- How different classes can work together to solve a problem.
- The importance of separating responsibilities between classes.
- How using objects makes code more reusable and scalable.
- Why OOP is preferred for larger Python projects.

---

## 🔄 Difference from Day 15

| Day 15 | Day 16 |
|--------|--------|
| Procedural Programming | Object-Oriented Programming |
| Most logic written in one file | Logic divided into multiple classes |
| Manual resource management | Managed by `CoffeeMaker` class |
| Manual money calculations | Managed by `MoneyMachine` class |
| Less modular | More modular and reusable |

---

## 🎯 Project Status

✅ Completed

---

## 🚀 Part of

This project is part of my **100 Days of Python** challenge where I build a new Python project every day while learning new concepts and improving my programming skills.

---

### ⭐ If you liked this project, feel free to star the repository!