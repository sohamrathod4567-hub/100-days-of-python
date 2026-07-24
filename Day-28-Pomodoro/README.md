# 🍅 Day 28 - Pomodoro Timer

## Overview

On Day 28 of the **100 Days of Python** course, I built a **Pomodoro Timer** using Python's **Tkinter** library. This project follows the Pomodoro productivity technique by alternating between focused work sessions and breaks while automatically tracking completed work sessions.

## Features

* ⏱️ 25-minute work sessions
* ☕ 5-minute short breaks
* 🌴 20-minute long break after every four work sessions
* ▶️ Start button to begin the timer
* 🔄 Reset button to stop and restart the timer
* ✅ Progress checkmarks displayed after each completed work session
* 🎨 Simple graphical interface built with Tkinter

## Concepts Practiced

* Tkinter GUI development
* Canvas widgets and images
* Labels and buttons
* Event-driven programming
* The `after()` method for countdown timers
* Global variables
* Functions and program flow
* Countdown logic
* Conditional statements
* String formatting
* Time calculations (minutes and seconds)

## Project Structure

```text
Day-28/
│── main.py
│── tomato.png
└── README.md
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

2. Navigate to the project:

```bash
cd Day-28
```

3. Run the program:

```bash
python main.py
```

## Example

```text
Timer: WORK
24:59

✔

Timer: BREAK
04:59

✔✔

Timer: WORK
24:59
```

## What I Learned

* How to create graphical applications using Tkinter.
* How to update the GUI dynamically without freezing the application.
* How the `after()` function schedules repeated tasks.
* Managing application state with global variables.
* Building a complete timer application using Python.
* Structuring GUI applications into reusable functions.

## Project Status

✅ Completed

This project marks my first productivity-focused desktop application using Tkinter and helped me understand how event-driven GUI programs work in Python.
