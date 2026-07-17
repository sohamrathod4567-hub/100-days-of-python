# 🐍 Day 21 – Snake Game (Part 2)

## 📖 Overview

On Day 21 of the **100 Days of Python** challenge, I continued building the classic **Snake Game**.

In this part, I added the core gameplay mechanics by introducing food, snake growth, and a live scoreboard. The snake now increases in length every time it eats food, while the score updates in real time, making the game interactive and much closer to the final version.

---

## 🚀 Concepts Practiced

* Object-Oriented Programming (OOP)
* Creating Multiple Classes
* Inheritance of Game Objects
* Random Module
* Collision Detection
* Working with Coordinates
* Updating Objects Dynamically
* Writing Text with Turtle
* File Organization
* Screen Animation

---

## ▶️ How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Run:

```bash
python main.py
```

---

## 🎮 Features Implemented

* ✅ Added randomly spawning food.
* ✅ Detects when the snake eats the food.
* ✅ Snake grows by one segment after eating.
* ✅ Food respawns at a new random location.
* ✅ Live scoreboard displays the current score.
* ✅ Smooth gameplay using Turtle graphics.

---

## 📸 Gameplay

```text
Score: 5

        🍎

◼ ◼ ◼ ◼ ►
```

*The snake grows longer every time it eats the food.*

---

## 📚 What I Learned

* Creating separate classes for different game components.
* Detecting collisions using object distance.
* Dynamically adding objects to an existing list.
* Updating text on the screen efficiently.
* Organizing a project into multiple Python files for better readability.

---

## 📂 Project Structure

```text
Day-21/
│── main.py
│── snake.py
│── food.py
│── scoreboard.py
```

---

## 🔜 Coming Next

* 💥 Detect wall collisions.
* 🐍 Detect collisions with the snake's own body.
* ☠️ Display a Game Over message.
* 🔄 Add the ability to restart the game.

---

## 📌 Project Status

🟢 **Day 21 Complete** — The Snake Game now includes food, snake growth, and a functioning scoreboard. The remaining work is to implement collision detection and game-over logic to complete the game.
