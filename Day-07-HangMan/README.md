# Day 7 - Hangman Game

## Overview

This is my seventh project from the **100 Days of Code: The Complete Python Pro Bootcamp**.

In this project, I built a fully functional **Hangman** game in Python. The player guesses letters to uncover a hidden word while trying to avoid running out of lives. The game uses separate modules to keep the code organized, including one for ASCII art and another for the word list.

## Project Structure

```text
Day-07-Hangman/
├── main.py
├── hangman_art.py
├── hangman_words.py
└── README.md
```

* **main.py** – Contains the game logic.
* **hangman_art.py** – Stores the ASCII art for the game logo and hangman stages.
* **hangman_words.py** – Contains the list of words used during gameplay.

## Concepts Practiced

* Functions
* `while` loops
* `for` loops
* Conditional statements (`if`, `elif`, `else`)
* Python Lists
* Strings
* Modules and importing files
* Variables
* Random module (`random.choice()`)
* Nested logic
* Tracking game state
* Preventing duplicate guesses
* ASCII art in Python

## How to Run

1. Clone this repository.
2. Navigate to the project folder.
3. Run the program:

```bash
py main.py
```

## ASCII Art

The game displays ASCII art stored in **`hangman_art.py`** to make the gameplay more interactive.

Example:

```text
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/
```

Example hangman stage:

```text
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
```

## Example

```text
Word to guess: _ _ _ _ _

Guess a letter: a

Correct!

Word to guess: _ a _ _ _

Guess a letter: e

Sorry, that's not in the word.

Lives remaining: 5
```

## What I Learned

* How to organize a Python project across multiple files using modules.
* How to import variables and functions from other Python files.
* How to build a complete terminal-based game.
* How to manage game state throughout multiple rounds.
* How to update the display after each guess.
* How to prevent users from guessing the same letter multiple times.
* How ASCII art can improve the user experience in terminal applications.
* How to combine loops, conditionals, functions, and modules into a larger project.

## Project Status

✅ Completed
