# Day 33 - ISS Overhead Notifier 🚀🛰️

## 📖 Overview

On **Day 33** of the **100 Days of Python Bootcamp**, I learned how to work with **APIs** by making HTTP requests using Python's `requests` library.

To apply these concepts, I built an **ISS Overhead Notifier** that checks the real-time location of the International Space Station (ISS). The program determines whether the ISS is currently within ±5° of my location and whether it is dark outside using the Sunrise-Sunset API. If both conditions are true, it automatically sends me an email notification so I know it's a good time to look up and try to spot the ISS.

---

## 🛠️ Concepts Practiced

- Working with REST APIs
- Making HTTP requests using the `requests` library
- Parsing JSON responses
- Using multiple APIs in one project
- Exception handling with `raise_for_status()`
- Working with latitude and longitude
- Comparing geographical coordinates
- Using the Sunrise-Sunset API
- Working with dates and times using `datetime`
- Sending emails with `smtplib`
- Using secure app passwords for email authentication
- Organizing code with reusable functions

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

### 2. Navigate to the project folder

```bash
cd Day-33-ISS-Overhead-Notifier
```

### 3. Install the required dependency

```bash
pip install requests
```

### 4. Configure the project

Before running the program, update the following values in `main.py`:

- Your latitude
- Your longitude
- Your email address
- Your email app password

### 5. Run the program

```bash
python main.py
```

The application will:

1. Fetch the current ISS location.
2. Check if the ISS is within ±5° of your location.
3. Determine if it is currently nighttime.
4. Send you an email notification if both conditions are satisfied.

---

## 📂 Project Structure

```text
Day-33-ISS-Overhead-Notifier/
│
├── main.py
└── README.md
```

---

## 📸 Example Output

When the ISS is overhead during nighttime:

```text
Checking ISS location...

ISS is nearby.

Checking sunrise and sunset times...

It is currently dark.

Sending email notification...

Email sent successfully!
```

When the ISS is not nearby:

```text
Checking ISS location...

ISS is not overhead.
```

---

## 📚 What I Learned

- How REST APIs work and why they are useful.
- How to send GET requests in Python.
- How to extract useful information from JSON responses.
- How to work with real-world geographical data.
- How to combine information from multiple APIs into one application.
- How to determine whether it is currently day or night based on sunrise and sunset times.
- How to automate email notifications using Python's SMTP library.
- The importance of handling HTTP errors gracefully with `raise_for_status()`.

---

## 🔮 Future Improvements

- Automatically run the program every minute using PythonAnywhere or a scheduler.
- Add desktop notifications instead of emails.
- Integrate Telegram or Discord notifications.
- Display the ISS location on an interactive map.
- Support multiple saved locations.
- Store a log of every successful ISS pass.
- Build a graphical user interface (GUI) using Tkinter.

---

## 🎯 Project Status

✅ Completed

This project introduced me to working with live web APIs and showed how Python can interact with real-world data. It combines API requests, JSON parsing, geographical calculations, time-based logic, and email automation into one practical application.