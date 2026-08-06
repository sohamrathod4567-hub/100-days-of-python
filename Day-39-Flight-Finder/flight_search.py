import os
import requests
from dotenv import load_dotenv


load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.response = None
        self._api_key = os.getenv("SERP_API")
        self.end_point = "https://serpapi.com/search"
        self.params = {
            "engine": "google_flights",
            "departure_id": "STV"         ,
            "arrival_id":   "CDG"          ,
            "outbound_date": "2026-08-10"        ,
            "return_date":   "2026-09-10"        ,
            "type":"1",
            "adults":"1",
            "currency":"GBP",
            "api_key":self._api_key
        }

    def check_flights(self):
        self.response = requests.get(self.end_point,params=self.params)

        return self.response.json()
