import requests_cache
import os
from pprint import pprint
from dotenv import load_dotenv
from  datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight


tomorrow = datetime.today().date() + timedelta(days=1)
six_month_from_today = datetime.today().date() + timedelta(days=182)

load_dotenv()
requests_cache.install_cache()

SERP_API = os.getenv("SERP_API")

sheet_data = DataManager()
destination_data = sheet_data.get_destination_data()
pprint(destination_data)

search = FlightSearch()
flights = search.check_flights(
    origin_city_code="LHR",
    destination_city_code="CDG",
    from_time=tomorrow,
    to_time=six_month_from_today,
)
pprint(flights)

cheapest_flight = find_cheapest_flight(flights , return_date=six_month_from_today)
pprint(f"{destination_data[0]['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < destination_data[0]['lowestprice']:
    pprint(f"Lower Price Flight found to {destination_data[0]['city']}!!")
    sheet_data.update_lowest_price(destination_data[0]["id"], cheapest_flight.price)
