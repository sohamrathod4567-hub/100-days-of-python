import requests_cache
import os
from pprint import pprint
from dotenv import load_dotenv
from  datetime import datetime,timedelta
from flight_search import FlightSearch

tomorrow = datetime.today().date() + timedelta(days=1)
six_month_from_today = datetime.today().date() + timedelta(days=182)

load_dotenv()
requests_cache.install_cache()

from data_manager import DataManager
SERP_API = os.getenv("SERP_API")

sheet_data = DataManager().get_destination_data()
pprint(sheet_data)

search = FlightSearch()
flights = search.check_flights(
    origin_city_code="LHR",
    destination_city_code="CDG",
    from_time=tomorrow,
    to_time=six_month_from_today,
)
pprint(flights)
