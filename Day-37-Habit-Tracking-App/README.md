# 📈 Day 37 - Habit Tracking App

A Python application built as part of the **100 Days of Code: The Complete Python Pro Bootcamp**. This project introduces working with REST APIs by integrating with the **Pixela** service to create and manage habit tracking graphs.

## 📖 Overview

The Habit Tracking App allows users to create a Pixela account, set up a graph for tracking a habit, and record daily progress through API requests. It demonstrates how Python can interact with web services using HTTP methods and JSON data.

## ✨ Features

- 👤 Create a Pixela user account
- 📊 Create a habit tracking graph
- ➕ Add a daily habit entry (pixel)
- ✏️ Update an existing entry
- 🗑️ Delete an existing entry
- 🔐 Authenticate requests using custom HTTP headers
- 🌐 Communicate with a REST API using Python

## 🛠️ Technologies Used

- Python 3
- Requests Library
- Pixela API
- REST APIs
- JSON

## 🧠 Concepts Practiced

- Making HTTP requests with `requests`
- REST API fundamentals
- HTTP methods:
  - `POST`
  - `PUT`
  - `DELETE`
- Sending JSON request bodies
- Working with API endpoints
- Using HTTP headers for authentication
- Handling API responses
- Reading API documentation
- String formatting with f-strings

## 📂 Project Structure

```
Day-37-Habit-Tracking-App/
│── main.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

### 2. Navigate to the project

```bash
cd Day-37-Habit-Tracking-App
```

### 3. Install dependencies

```bash
pip install requests
```

### 4. Create a Pixela account

Visit:

https://pixe.la/

or create one using the API from the project.

### 5. Configure your credentials

Update the following variables in `main.py`:

```python
USERNAME = "your_username"
TOKEN = "your_token"
```

### 6. Run the project

```bash
python main.py
```

## 📸 Example

### Create a Graph

```python
graph_config = {
    "id": "graph1",
    "name": "BookReading",
    "unit": "Pages",
    "type": "float",
    "color": "ajisai"
}
```

### Successful Response

```text
{"message":"Success.","isSuccess":true}
```

## 📚 What I Learned

- How REST APIs are structured.
- The difference between `GET`, `POST`, `PUT`, and `DELETE` requests.
- How to send JSON data using the `json=` parameter.
- How HTTP headers are used for authentication.
- How to read and implement API documentation.
- How to debug API responses and identify request formatting issues.
- The difference between sending data as form data (`data=`) and JSON (`json=`).
- How external services can be integrated into Python applications.

## 🎯 Project Status

✅ Completed

This project marks my first hands-on experience with building a Python application that communicates with an external REST API. It strengthened my understanding of HTTP requests, JSON payloads, authentication headers, and working with real-world web services.

---

### 📅 Part of

**100 Days of Code: The Complete Python Pro Bootcamp**

**Day 37 Project – Habit Tracking App**