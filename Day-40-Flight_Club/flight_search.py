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
        self.stops = 0

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        if is_direct:
            self.stops =  0
        else:
            self.stops = 1
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "currency": "GBP",
            "api_key": self._api_key,
            "stops": self.stops
        }
        response = requests.get(self.end_point, params=query)

        if response.status_code != 200:
            print(f"Check_flights() Response code : {response.status_code}")
            return None

        data = response.json()
        if "error" in data :
            print(f"API ERROR : {data['error']}")
            return None
        return data