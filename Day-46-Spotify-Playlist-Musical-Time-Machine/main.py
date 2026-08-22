import requests
from bs4 import BeautifulSoup

date = input("What Year do you want to travel to ? (YYYY-MM-DD):")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(URL)
bill_bord_web_page = response.text
print(bill_bord_web_page)

# soup = BeautifulSoup.text
