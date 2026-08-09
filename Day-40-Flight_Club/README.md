# Day 40 – Flight Club ✈️

## Overview

Day 40 of the **100 Days of Code – The Complete Python Pro Bootcamp** focused on building a **Flight Club** application.

The project uses flight search APIs and a spreadsheet/database to store customer information and search for cheap flight deals. The application can retrieve customer data, search for flights, compare prices, and prepare flight deal notifications.

This project combines multiple APIs and Python modules to create a more practical real-world application.

---

## Concepts Practiced

* Working with APIs
* Making `GET` requests using `requests`
* Processing JSON responses
* Working with lists of dictionaries
* Object-Oriented Programming (OOP)
* Creating and using classes
* Class methods
* Reading data from a spreadsheet API
* Searching for flight information
* Working with dates
* Using environment variables
* Handling API responses
* Importing and organizing Python modules
* Using external APIs in a Python project

---

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the Day 40 project:

```bash
cd Day-40-Flight_Club
```

3. Install the required dependencies:

```bash
pip install requests python-dotenv
```

4. Create a `.env` file and add your API credentials:

```env
SHEETY_ENDPOINT=your_sheety_endpoint
SHEETY_USERNAME=your_username
SHEETY_PASSWORD=your_password
TEQUILA_API_KEY=your_api_key
```

5. Run the program:

```bash
python main.py
```

> **Note:** Never upload API keys, passwords, tokens, or other sensitive credentials to GitHub.

---

## Example

The application can retrieve customer information from the spreadsheet:

```text
Customer: Soham
Email: soham@example.com
```

It can then search for available flight deals and compare them against the desired prices.

Example output:

```text
Searching for flights...

Cheap flight found!

From: BOM
To: PAR
Price: €320
```

---

## What I Learned

During Day 40, I learned how to combine multiple APIs in a single Python project and work with structured JSON data.

I also practiced handling lists containing dictionaries, which is important when working with API responses.

The project helped me understand how Python can be used to build applications that interact with real-world services such as flight-search APIs and online spreadsheets.

I also gained more experience with Object-Oriented Programming and organizing a larger Python project into separate modules.

---

## Project Status

**Completed** ✅

Day 40 completed as part of my **100 Days of Code – The Complete Python Pro Bootcamp** journey.
