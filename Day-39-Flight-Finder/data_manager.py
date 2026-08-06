import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()
SHEETY_API_ENDPOINT = os.getenv("SHEETY_API")
USERNAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
AUTHORIZATION = HTTPBasicAuth(USERNAME, PASSWORD)

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):

        self.destination_data = {}
    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT, auth=AUTHORIZATION)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data