# 🎯 Day 12 - Number Guessing Game

## 📖 Overview

On Day 12 of the **100 Days of Python** challenge, I built a **Number Guessing Game** where the player has to guess a randomly generated number between **1 and 100**.

The game includes two difficulty levels:

* **Easy Mode** – 10 lives
* **Hard Mode** – 5 lives

After every incorrect guess, the game provides feedback indicating whether the guess was **too high** or **too low**, helping the player narrow down the correct answer. Once the game ends, the player can choose to play again without restarting the program.

---

## 🧠 Concepts Practiced

* Functions
* `while` loops
* Conditional statements (`if`, `elif`, `else`)
* Random number generation using `random.randint()`
* User input handling
* Replay game logic
* Difficulty selection
* Variables and counters
* Importing modules
* Code organization

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the **Day-12** folder.
3. Make sure Python is installed.
4. Run the program:

```bash
python main.py
```

---

## 🎮 Example

```text
Welcome to the Number Guessing Game

Choose difficulty: Easy (e) or Hard (h): e

You now have 10 lives left.

Guess a number between 1 and 100: 50
Too high.
You have 9 lives left.

Guess a number between 1 and 100: 25
Too low.
You have 8 lives left.

Guess a number between 1 and 100: 37
You guessed the number right! It was 37.
You win!

Do you want to play again? (y/n)
```

---

## 📚 What I Learned

* How to organize a complete program using functions.
* How to create different game difficulty levels.
* How to use loops to keep a game running until the player wins or loses.
* How to provide meaningful feedback after each user guess.
* How to restart a program without closing it by using a replay loop.
* How to write cleaner and more structured Python code.

---

## ✅ Project Status

**Completed ✔️**

This project is part of my **100 Days of Python** journey. More projects and improvements will be added as I continue learning Python.
