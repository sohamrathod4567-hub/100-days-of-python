# 🏓 Day 22 - Pong Arcade Game

A recreation of the classic **Pong Arcade Game** using Python's **Turtle Graphics** module. This project focuses on applying Object-Oriented Programming concepts by breaking the game into multiple classes such as paddles, ball, and scoreboard while implementing real-time game mechanics. The project follows Day 22 of the **100 Days of Code: The Complete Python Pro Bootcamp**. :contentReference[oaicite:0]{index=0}

---

## 📖 Overview

This project recreates one of the most iconic arcade games ever made. Two paddles compete to keep the ball in play. Each time a player misses the ball, the opponent earns a point. As the game progresses, the ball speeds up, making the gameplay more challenging.

---

## 🚀 Features

- 🎮 Two-player Pong gameplay
- 🏓 Smooth paddle movement
- ⚪ Ball movement with realistic bouncing
- 🚧 Collision detection with walls and paddles
- 📈 Increasing ball speed after every successful hit
- 🧮 Live scoreboard
- 🔄 Ball reset after each point
- 🖥️ Clean object-oriented project structure

---

## 🧠 Concepts Practiced

- Object-Oriented Programming (OOP)
- Creating custom classes
- Inheritance
- Turtle Graphics
- Keyboard event listeners
- Collision detection
- Animation loops
- Screen updates with `tracer()`
- Timers using `time.sleep()`
- Modular programming

---

## 📂 Project Structure

```
Day-22/
│── main.py
│── paddle.py
│── ball.py
│── scoreboard.py
```

---

## 🎮 Controls

| Player | Move Up | Move Down |
|--------|---------|-----------|
| Left Paddle | W | S |
| Right Paddle | ↑ | ↓ |

---

## ▶️ How to Run

1. Clone this repository.

```bash
git clone <your-repository-url>
```

2. Navigate to the project folder.

```bash
cd Day-22
```

3. Run the game.

```bash
python main.py
```

---

## 💻 Example Gameplay

```
Left Player: 4

          ⚪

        █
                    █

Right Player: 3
```

The ball bounces off the paddles and top/bottom walls. If a player misses the ball, the opponent scores a point and the ball resets.

---

## 📚 What I Learned

- How to divide a large project into smaller classes
- Managing multiple objects simultaneously
- Detecting collisions between moving objects
- Using object composition in game development
- Building a continuous game loop
- Improving game feel by dynamically increasing difficulty
- Writing cleaner, reusable, and modular code

---

## 📌 Project Status

✅ Completed

Day 22 of the **100 Days of Python** challenge successfully completed.
The Pong Arcade Game is fully playable with two-player controls, score tracking, collision detection, and progressively faster gameplay.

---
```