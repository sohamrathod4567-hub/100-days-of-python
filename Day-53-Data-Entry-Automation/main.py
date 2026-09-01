import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re

URL = "https://appbrewery.github.io/Zillow-Clone/"

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc7vMuMtdjXJAqHWnpg37f17tGHsAqk2Kvn_PnNU6qJGoiM9A/viewform?usp=publish-editor"

response = requests.get(URL)
zillow_web_page = response.text

addy = []
price = []
links = []


soup = BeautifulSoup(zillow_web_page, "html.parser")
# print(soup.prettify())
all_addresses = soup.find_all("address", attrs={"data-test": "property-card-addr"})
# print(all_addresses)

for address in all_addresses:
    addy.append(address.get_text(strip=True))

# print(addy)

all_prices = soup.find_all(    "span",
    attrs={"data-test": "property-card-price"}
)

for p in all_prices:
    price_text = p.get_text(strip=True)
    price_only = re.search(r"\$[\d,]+", price_text).group()
    # print(price_only)
    price.append(price_only)

# print(price)