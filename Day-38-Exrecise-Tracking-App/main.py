import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("REAL_API_KEY")
DATE = datetime.today().strftime('%d/%m/%y')
TIME = datetime.today().strftime('%H:%M:%S')
USERNAME = os.getenv("UNAME")
PASSWORD = os.getenv("PASS")

print(DATE)
print(TIME)
user_data = input("What form of exercise have you done today?")
today = datetime.today().strftime('%d/%m/%y')

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

headers = {
    "Content-Type" : "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {
    "query" : user_data
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
print(result)

sheety_endpoint = "https://api.sheety.co/1adae7ed9024997cddf849e6355a05ab/copyOfMyWorkouts/workouts"
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(sheety_endpoint, json=sheet_inputs ,auth=(USERNAME, PASSWORD))
    print(response.text)