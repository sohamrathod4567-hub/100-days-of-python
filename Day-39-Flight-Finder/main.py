import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

from data_manager import DataManager
SERP_API = os.getenv("SERP_API")

sheet_data = DataManager()
pprint(sheet_data.prices)
