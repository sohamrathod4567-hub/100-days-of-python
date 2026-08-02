# 🌤️ Day 36 - Stock Trading News Alert

A Python application that monitors stock price movements using the Alpha Vantage API and fetches the latest news articles using the NewsAPI. If a significant change in the stock price is detected, the program displays relevant news headlines that help explain the market movement.

---

# 📖 Overview

In this project, I learned how to combine data from multiple APIs to build a useful real-world application.

The application:

* Retrieves the latest stock price data.
* Calculates the percentage change between consecutive trading days.
* Determines whether the change exceeds a predefined threshold.
* Fetches recent news articles related to the company.
* Formats the news into an easy-to-read alert.

This project demonstrates how different APIs can work together to provide meaningful information.

---

# 🚀 Concepts Practiced

* Working with multiple REST APIs
* Making HTTP requests using the `requests` library
* JSON parsing
* Dictionary and list manipulation
* Percentage calculations
* Conditional statements
* Environment variables for API keys
* String formatting with f-strings
* Data filtering

---

# 🛠️ Technologies Used

* Python
* Requests
* Alpha Vantage API
* NewsAPI

---

# ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/your-username/100-Days-of-Python.git
```

2. Navigate to the project folder.

```bash
cd Day-36-Stock-Trading-News
```

3. Install the required package.

```bash
pip install requests
```

4. Add your API keys.

```python
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
```

5. Run the program.

```bash
python main.py
```

---

# 📂 Project Flow

```
Get Stock Data
       │
       ▼
Calculate Price Change
       │
       ▼
Change > Threshold?
   │             │
  No            Yes
   │             │
   ▼             ▼
  Exit     Fetch News Articles
                 │
                 ▼
        Display Headlines
```

---

# 💡 Example Output

```
TSLA: 🔺5%

Headline: Tesla shares surge after quarterly earnings.

Brief: Investors responded positively to stronger-than-expected revenue and delivery numbers.

--------------------------------------------------
```

---

# 📚 What I Learned

* How stock market data is structured.
* How to calculate percentage changes between trading days.
* How to integrate multiple APIs into a single application.
* How to filter and display only useful information.
* How external APIs can be combined to build practical automation tools.

---

# 🔮 Possible Improvements

* Send notifications via email.
* Integrate Telegram or Discord alerts.
* Support multiple stocks.
* Schedule the script to run automatically every morning.
* Build a simple dashboard using Flask or Streamlit.
* Store historical alerts in a database.

---

# 📁 Project Structure

```
Day-36-Stock-Trading-News/
│── main.py
│── README.md
```

---

# 🎯 Project Status

**✅ Stock Price Monitoring:** Complete

**✅ News Fetching:** Complete

**📅 Day:** 36 / 100

---

Part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Dr. Angela Yu.
