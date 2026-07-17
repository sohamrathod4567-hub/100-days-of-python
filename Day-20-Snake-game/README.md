# 🐍 Day 20 – Snake Game (Part 1)

## 📖 Overview

Day 20 begins the development of the classic **Snake Game** as part of the **100 Days of Python** challenge.

In this part, the focus was on building the foundation of the game. A snake was created using multiple turtle objects, movement logic was implemented, and keyboard controls were added so the player can control the snake's direction. This establishes the core mechanics that future parts will build upon.

---

## 🚀 Concepts Practiced

* Object-Oriented Programming (OOP)
* Python Classes and Objects
* Lists
* Loops
* Methods
* Keyboard Event Listeners
* Screen Updates with `tracer()`
* Animation using `screen.update()`
* `time.sleep()`
* Turtle Graphics
* Absolute Direction Control with `setheading()`

---

## ▶️ How to Run

1. Clone this repository.
2. Open the project folder.
3. Run:

```bash
python main.py
```

---

## 🎮 Features Implemented

* ✅ Created the snake using multiple turtle segments.
* ✅ Added continuous snake movement.
* ✅ Connected the arrow keys for movement.
* ✅ Prevented the snake from making a 180° turn.
* ✅ Used `screen.tracer(0)` and `screen.update()` for smooth animation.
* ✅ Organized the snake logic inside its own `Snake` class.

---

## 📸 Gameplay

```text
        ▲
        │
◼ ◼ ◼
```

Use the **Arrow Keys** to control the snake.

---

## 📚 What I Learned

* Building a game using Object-Oriented Programming.
* Managing multiple objects as a single entity.
* Creating smooth animations with Turtle graphics.
* Handling keyboard events in Python.
* Updating object positions by moving each segment to the previous segment's location.
* Restricting opposite-direction movement for better gameplay.

---

## 🔜 Coming Next

* 🍎 Add food generation.
* 📈 Create a scoreboard.
* 🐍 Grow the snake after eating food.
* 💥 Detect collisions with walls.
* ☠️ Detect collisions with the snake's own body.
* 🔄 Add a game-over and restart system.

---

## 📌 Project Status

🟢 **Day 20 Complete** — The snake is fully controllable and the core movement mechanics are working. The game foundation is now ready for food, scoring, and collision detection in the next stage.
