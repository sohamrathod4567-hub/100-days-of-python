import requests
import os
from dotenv import load_dotenv
load_dotenv()
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API")
USERNAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.response = requests.get(SHEETY_API_ENDPOINT,auth=(USERNAME, PASSWORD))
        self.prices = self.response.json()