# Day 34 - Quizzler App 🧠

## Overview

Day 34 focused on building **Quizzler**, a graphical True/False quiz application using **Tkinter**. In this project, I learned how to consume data from an API, parse JSON responses, and display questions through a clean GUI. The application provides instant feedback by changing the background color based on the user's answer while keeping track of the score.

This project introduced the concept of separating the application's logic from its user interface, making the code more organized and maintainable.

---

## Concepts Practiced

- Working with APIs using the `requests` library
- Parsing JSON data
- Object-Oriented Programming (OOP)
- Building graphical interfaces with Tkinter
- Using `Canvas`, `Label`, and `Button` widgets
- Event-driven programming
- Updating UI elements dynamically
- Using `after()` for timed events
- Separating UI and business logic
- Managing application state
- Working with classes across multiple files

---

## Features

- Fetches quiz questions from the Open Trivia Database API
- Displays one question at a time
- True and False answer buttons
- Instant visual feedback:
  - 🟢 Green for correct answers
  - 🔴 Red for incorrect answers
- Live score tracking
- Automatically loads the next question
- Disables answer buttons when the quiz ends
- Clean and responsive Tkinter interface

---

## Project Structure

```
Day-34-Quizzler/
│── main.py
│── ui.py
│── quiz_brain.py
│── question_model.py
│── data.py
│── images/
│   ├── true.png
│   └── false.png
│── requirements.txt
└── README.md
```

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

2. Navigate to the project folder:

```bash
cd Day-34-Quizzler
```

3. Install the required package:

```bash
pip install requests
```

4. Run the application:

```bash
python main.py
```

---

## Example

```
Question:
The Great Wall of China is visible from space.

Your Answer: False

✅ Correct!

Score: 5
```

---

## What I Learned

- How to fetch live data from an API
- How JSON responses are structured
- Creating and updating Tkinter widgets
- Using Canvas to display dynamic text
- Handling button click events
- Updating labels and canvas content dynamically
- Providing visual feedback to users
- Using `window.after()` to delay actions
- Designing applications using multiple classes
- Keeping UI and application logic separate

---

## Technologies Used

- Python 3
- Tkinter
- Requests
- Open Trivia Database (OpenTDB) API
- Object-Oriented Programming (OOP)

---

## Future Improvements

- Add multiple difficulty levels
- Allow users to select quiz categories
- Add a timer for each question
- Display a final score summary
- Save high scores locally
- Add sound effects and animations
- Include a restart quiz button

---

## Project Status

✅ Completed

This project strengthened my understanding of working with APIs and building desktop GUI applications with Tkinter. It also reinforced the importance of separating application logic from the user interface using Object-Oriented Programming principles.