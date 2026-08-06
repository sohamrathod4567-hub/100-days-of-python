import requests_cache
import os
from pprint import pprint
from dotenv import load_dotenv
from  datetime import datetime,timedelta

tomorrow = datetime.today() + timedelta(days=1)
six_month_from_today = datetime.today() + timedelta(days=182)

load_dotenv()
requests_cache.install_cache()

from data_manager import DataManager
SERP_API = os.getenv("SERP_API")

sheet_data = DataManager()
pprint(sheet_data.prices)
