# 🧠 Day 17 – Quiz Game (OOP & Modularity)

## 📖 Overview

On Day 17 of the **100 Days of Python** challenge, I built a **True/False Quiz Game** using the principles of **Object-Oriented Programming (OOP)** and **modular programming**.

Instead of writing everything in a single file, I separated the project into multiple modules, making the code cleaner, easier to understand, and more maintainable. The program reads quiz questions, asks the user for answers, checks whether they are correct, and keeps track of the score throughout the game.

---

## 🛠️ Concepts Practiced

* Classes and Objects
* Constructors (`__init__`)
* Object Composition
* Encapsulation
* Modular Programming
* Importing Custom Python Modules
* Lists of Objects
* Loops
* User Input
* Conditional Statements
* Tracking Score
* Working with External Data

---

## 📂 Project Structure

```text
Day-17-Quiz-Game/
│── main.py
│── quiz_brain.py
│── question_model.py
│── data.py
```

* **main.py** → Creates the quiz and controls the game loop.
* **question_model.py** → Defines the `Question` class.
* **quiz_brain.py** → Handles quiz logic, scoring, and user interaction.
* **data.py** → Stores all quiz questions and answers.

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone https://github.com/sohamrathod4567-hub/100-days-of-python.git
```

2. Navigate to the project folder.

```bash
cd 100-days-of-python/Day-17-Quiz-Game
```

3. Run the program.

```bash
python main.py
```

---

## 💻 Example

```text
Q.1: A slug's blood is green. (True / False): True
Correct!
Correct Answer: True
Your current score is: 1/1

Q.2: The loudest animal is the elephant. (True / False): False
Correct!
Correct Answer: False
Your current score is: 2/2
```

---

## 📚 What I Learned

* How to organize a project using multiple Python modules.
* How different classes can work together to build an application.
* How to create and use custom objects.
* How to separate data, logic, and user interaction.
* The importance of reusable and maintainable code through OOP.

---

## 🚀 Project Status

✅ Completed – Day 17 of the **100 Days of Python** challenge.
