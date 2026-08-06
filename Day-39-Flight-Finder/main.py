import requests_cache
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()
requests_cache.install_cache()

from data_manager import DataManager
SERP_API = os.getenv("SERP_API")

sheet_data = DataManager()
pprint(sheet_data.prices)
