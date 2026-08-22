import requests
from bs4 import BeautifulSoup

date = input("What Year do you want to travel to ? (YYYY-MM-DD):")
URL = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

response = requests.get(URL)
bill_bord_web_page = response.text
# print(bill_bord_web_page)

soup = BeautifulSoup(bill_bord_web_page, "html.parser")
song_titles=soup.find(name="h3",class_="chart-entry__title")
print(song_titles)