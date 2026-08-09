import requests_cache
import os
from pprint import pprint
from dotenv import load_dotenv
from  datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

tomorrow = datetime.today().date() + timedelta(days=1)
six_month_from_today = datetime.today().date() + timedelta(days=182)

load_dotenv()
requests_cache.install_cache()

SERP_API = os.getenv("SERP_API")

sheet_data = DataManager()
destination_data = sheet_data.get_destination_data()
pprint(destination_data)
search = FlightSearch()

message = []

ORIGIN_CITY_IATA = "LHR"
for destination in destination_data:
    pprint(f"Getting Flights for {destination["city"]}...")
    flights = search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    pprint(flights)

    cheapest_flight = find_cheapest_flight(flights , return_date=six_month_from_today)
    message.append(f"{destination['city']}: GBP {cheapest_flight.price}")

    if cheapest_flight.price == "N/A":
        flights = search.check_flights(
            origin_city_code=ORIGIN_CITY_IATA,
            destination_city_code=destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False,
        )

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination['lowestPrice']:
        message.append(f"Lower Price Flight found to {destination['city']}!!")
        sheet_data.update_lowest_price(destination["id"],cheapest_flight.price)

email = NotificationManager(message)

customer_email = sheet_data.get_customer_emails()

print(customer_email)
