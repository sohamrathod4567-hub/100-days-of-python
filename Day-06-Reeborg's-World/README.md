# Day 6 - Functions, While Loops & Reeborg's World Maze

## Overview

This is my sixth project from the **100 Days of Code: The Complete Python Pro Bootcamp**.

Day 6 introduced two of Python's most important concepts: **functions** and **while loops**. Instead of building a traditional command-line application, I practiced solving maze challenges using **Reeborg's World**, an interactive platform designed to improve problem-solving and programming logic.

The objective was to guide the robot through different maze layouts by writing reusable functions and implementing efficient movement logic until the robot successfully reached the goal.

## Project Platform

This project was completed using **Reeborg's World**, an online environment for learning programming through interactive robot challenges.

**Practice Website:**

* https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

## Concepts Practiced

* Creating user-defined functions using `def`
* Calling functions
* Code reusability
* Function decomposition
* `while` loops
* Conditional statements (`if`, `elif`, `else`)
* Problem-solving using programming logic
* Code indentation
* Infinite loop prevention
* Maze-solving algorithms

## Key Learnings

### Functions

Functions allow us to group a block of code under a single name so it can be reused whenever needed. Instead of writing the same code multiple times, we can simply call the function.

Example:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```

A function executes only when it is called:

```python
turn_right()
```

### While Loops

A `while` loop continues executing as long as its condition remains true.

```python
while condition:
    # Code to execute
```

Unlike a `for` loop, a `while` loop is best used when the number of iterations is unknown beforehand. It is important to ensure that the condition eventually becomes false to avoid creating an infinite loop.

### For Loop vs While Loop

**Use a `for` loop when:**

* The number of iterations is known.
* Iterating through lists or sequences.

**Use a `while` loop when:**

* The number of iterations is unknown.
* The program should continue until a specific condition is met.

## How to Run

This project is designed to run inside **Reeborg's World**.

1. Open the Reeborg's World website.
2. Select the Maze challenge.
3. Copy your Python solution into the editor.
4. Run the program to watch the robot solve the maze.

## Example Logic

The maze solution uses helper functions to simplify movement and repeatedly checks the robot's surroundings until the destination is reached.

Example structure:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    if right_is_clear():
        turn_right()
        move()
    elif wall_on_right():
        turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()
```

## Tips & Notes

* Proper indentation is essential in Python.
* One indentation level equals **4 spaces** (or one tab, depending on your editor settings).
* Keyboard shortcut in VS Code:

  * **Ctrl + ]** → Increase indentation for selected code.
* When debugging, always verify your assumptions before changing the code.

## What I Learned

* How to create and reuse custom functions.
* The difference between defining and calling a function.
* How `while` loops work and when to use them.
* The importance of clean code through reusable functions.
* How to solve algorithmic problems by breaking them into smaller tasks.
* How to navigate maze challenges using logical decision-making.
* Why maintaining proper indentation is critical in Python.

## Project Status

✅ Completed
