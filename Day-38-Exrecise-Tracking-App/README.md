# Day 38 - Exercise Tracking App 🏃‍♂️

## 📌 Overview

On Day 38 of the **100 Days of Python** challenge, I built an **Exercise Tracking App** that uses Natural Language Processing (NLP) to understand workout descriptions and automatically logs them into a Google Sheet.

The application takes a user's exercise input in plain English, sends it to the **Nutritionix Exercise API**, receives detailed workout information (such as exercise name, duration, and calories burned), and then stores the results using the **Sheety API**.

This project demonstrates how multiple APIs can be combined to automate everyday tasks.

---

## 🚀 Features

* Accepts exercise descriptions in natural language.
* Uses the Nutritionix API to identify exercises.
* Calculates:

  * Exercise performed
  * Duration
  * Calories burned
* Automatically records workout data into a Google Sheet.
* Uses environment variables to securely store API credentials.
* Logs the current date and time for every workout entry.

---

## 🛠️ Technologies Used

* Python 3
* Requests
* Python Dotenv
* Nutritionix Exercise API
* Sheety API
* Environment Variables (.env)

---

## 📂 Project Structure

```text
Day-38-Exercise-Tracking-App/
│
├── main.py
├── .env                # Not committed to GitHub
├── .gitignore
└── README.md
```

---

## 📖 Concepts Practiced

* Working with REST APIs
* HTTP POST requests
* JSON data handling
* Request headers
* Authentication with API keys
* Environment variables
* Reading secrets using `python-dotenv`
* Date and time formatting
* Looping through API responses
* Automating data entry

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

### 2. Navigate to the project

```bash
cd Day-38-Exercise-Tracking-App
```

### 3. Install dependencies

```bash
pip install requests python-dotenv
```

### 4. Create a `.env` file

```text
APP_ID=your_nutritionix_app_id
REAL_API_KEY=your_nutritionix_api_key
UNAME=your_sheety_username
PASS=your_sheety_password
```

> **Important:** Never commit your `.env` file to GitHub.

### 5. Run the program

```bash
python main.py
```

---

## 💻 Example

```text
What form of exercise have you done today?

Ran 5 km and cycled for 20 minutes
```

Example workout logged:

| Date     | Time     | Exercise | Duration | Calories |
| -------- | -------- | -------- | -------: | -------: |
| 06/08/26 | 13:45:10 | Running  |   30 min |      352 |
| 06/08/26 | 13:45:10 | Cycling  |   20 min |      184 |

---

## 📚 What I Learned

* How to work with APIs that require authentication headers.
* The importance of storing sensitive credentials securely using environment variables.
* How Natural Language Processing APIs can interpret user input.
* How to chain multiple APIs together to build an automated workflow.
* How to send structured data to Google Sheets using the Sheety API.
* Better debugging techniques for API responses and authentication issues.

---

## 🔒 Security

This project uses a `.env` file to keep API keys and credentials private.

The `.env` file is excluded from version control using `.gitignore`.

---

## 🎯 Project Status

✅ Completed

**Day 38 of the 100 Days of Python Challenge**
