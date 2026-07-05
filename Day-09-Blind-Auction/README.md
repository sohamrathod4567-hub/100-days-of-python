# Day 09 - Secret Blind Auction 🏷️🔨

## 📖 Overview

On **Day 9** of the **100 Days of Python** challenge, I built a **Secret Blind Auction** program. Participants enter their name and bid amount one at a time, while keeping their bids hidden from other participants. Once all bids have been entered, the program determines and announces the highest bidder.

This project helped me gain a better understanding of **Python dictionaries**, **loops**, **functions**, and how to find the maximum value in a dictionary.

---

## 🧠 Concepts Practiced

- Python Dictionaries
- Storing key-value pairs
- Adding and updating dictionary entries
- `while` loops
- Conditional statements (`if` / `else`)
- User input handling
- Functions
- Finding the highest value using:

```python
max(details, key=details.get)
```

- Dictionary methods
- Basic program flow and logic

---

## ▶️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/100-days-of-python.git
```

2. Navigate to the project folder:

```bash
cd Day-09-Secret-Blind-Auction
```

3. Run the program:

```bash
python main.py
```

---

## 💻 Example

```text
What is your name?
Harry

How much do you bid?
$250

Are there any other bidders? (y/n)
y

What is your name?
Hermione

How much do you bid?
$430

Are there any other bidders? (y/n)
n

The winner is Hermione with a bid of $430!
```

---

## 📚 What I Learned

- How dictionaries can efficiently store and retrieve data.
- How to continuously collect user input using loops.
- The importance of updating dictionary values dynamically.
- How the built-in `max()` function works with the `key` parameter.
- Why `max(details, key=details.get)` is an elegant way to find the dictionary key with the highest value.
- Writing cleaner and more readable Python code using built-in functions.

---

## 🚀 Project Status

✅ Completed as part of the **100 Days of Python Bootcamp** challenge.

**Day 9 Complete ✔️**