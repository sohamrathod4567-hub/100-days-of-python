# ✈️ Day 39 - Flight Deal Finder (Part 1)

## Overview

Day 39 marks the beginning of the **Flight Deal Finder** project from the **100 Days of Python** course. This project is split into **two parts**:

* **Part 1 (Day 39):** Build the flight search system, compare flight prices with stored destination prices, update the Google Sheet when cheaper flights are found, and send email notifications.
* **Part 2 (Day 40):** Enhance the project by sending personalized flight deal notifications to users based on their saved information.

In this first part, the application automatically searches for flights using the **SerpAPI Google Flights API**, compares the latest prices against the stored prices in a Google Sheet managed through **Sheety**, and updates the sheet whenever a better deal is found.

---

## Features

* Retrieve destination data from a Google Sheet using the Sheety API.
* Search for flights using the SerpAPI Google Flights API.
* Find the cheapest available flight.
* Compare live flight prices with the stored lowest prices.
* Automatically update the Google Sheet when a lower price is found.
* Send email notifications whenever a cheaper flight is discovered.
* Securely manage API keys and credentials using environment variables.

---

## Concepts Practiced

* Working with REST APIs
* HTTP GET and PUT requests
* API Authentication
* Environment Variables (`python-dotenv`)
* Date and Time Manipulation (`datetime`, `timedelta`)
* Object-Oriented Programming (OOP)
* Working with JSON data
* Data comparison and filtering
* Sending Emails using SMTP
* Modular Python Project Structure

---

## Project Structure

```text
Day-39-Flight-Finder/
│
├── main.py
├── data_manager.py
├── flight_search.py
├── flight_data.py
├── notification_manager.py
├── .env
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* SerpAPI (Google Flights)
* Sheety API
* SMTP (Gmail)
* Requests
* requests-cache
* python-dotenv

---

## Environment Variables

Create a `.env` file and add your credentials:

```env
SERP_API=your_serpapi_key

SHEETY_ENDPOINT=your_sheety_endpoint
SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password

MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_gmail_app_password
```

> **Note:** If you're using Gmail, generate an **App Password** instead of using your regular account password.

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/yourusername/100-Days-of-Python.git
```

2. Navigate to the project folder.

```bash
cd Day-39-Flight-Finder
```

3. Install the required packages.

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your API keys and email credentials.

5. Run the project.

```bash
python main.py
```

---

## Example Output

```text
Getting Flights for Paris...

Cheapest Flight Found:
Paris : GBP 132

Lower Price Flight Found!

Updating Google Sheet...

Email Notification Sent Successfully.
```

---

## What I Learned

During this project, I learned how to:

* Integrate multiple APIs into a single application.
* Fetch and update data stored in Google Sheets using the Sheety API.
* Search real-time flight prices with SerpAPI.
* Compare live data against stored records.
* Build a modular Python project using classes.
* Send automated email notifications through SMTP.
* Store sensitive credentials securely using environment variables.
* Organize larger Python projects into multiple files for better readability and maintenance.

---

## Project Status

✅ **Day 39 (Part 1) Completed**

Completed:

* Destination data retrieval
* Flight searching
* Cheapest flight detection
* Price comparison
* Google Sheet updates
* Email notifications

**Coming in Day 40 (Part 2):**

* User registration
* Personalized notifications
* Sending flight deals directly to subscribed users
* Enhanced automation

---

## Course

This project is part of **Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp**.

Day 39 focuses on building the core flight price tracking system, while Day 40 expands it into a complete flight deal notification service.
