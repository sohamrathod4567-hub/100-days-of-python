# Day 31 - Flash Card App 🇫🇷

## Overview

On **Day 31** of the **100 Days of Code: Python Bootcamp**, I built a **Flash Card App** using **Tkinter**. The application helps users learn French vocabulary by displaying a French word on one side of a flashcard and automatically revealing its English translation after a few seconds.

The app also tracks learning progress by removing words that have already been mastered, making future study sessions more efficient.

---

## Features

* Interactive flashcard interface built with Tkinter.
* Automatically flips the card after a few seconds.
* Displays French words and their English translations.
* Mark words as **Known** or **Unknown**.
* Saves learning progress using CSV files.
* Loads saved progress when the application is reopened.
* Randomly selects a new word each round.

---

## Concepts Practiced

* Tkinter GUI development
* Canvas widgets and images
* Event handling with buttons
* `after()` method for timed events
* Reading and writing CSV files with Pandas
* Exception handling (`try` / `except`)
* Random data selection
* Data persistence
* Working with dictionaries and lists

---

## Project Structure

```text
Day-31-Flash-Card-App/
│── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   └── wrong.png
│
│── data/
│   ├── french_words.csv
│   └── words_to_learn.csv
│
│── main.py
└── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/100-days-of-python.git
```

2. Navigate to the project:

```bash
cd Day-31-Flash-Card-App
```

3. Install the required library:

```bash
pip install pandas
```

4. Run the application:

```bash
python main.py
```

---

## Example Workflow

```text
French Word:
bonjour

(Card flips after 3 seconds...)

English Translation:
hello

✔️ Known → Removes the word from future sessions.

❌ Unknown → Keeps the word for future practice.
```

---

## What I Learned

* Designing desktop applications with Tkinter.
* Managing timed events using `after()`.
* Reading, updating, and saving CSV data with Pandas.
* Creating a better user experience through a graphical interface.
* Persisting user progress between sessions.
* Combining GUI programming with file handling and data manipulation.

---

## Technologies Used

* Python 3
* Tkinter
* Pandas
* CSV Files

---

## Project Status

✅ Completed

This project is part of my **100 Days of Python** challenge and demonstrates how Python can be used to build practical desktop applications for language learning.
