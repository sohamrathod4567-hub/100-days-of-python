import requests
from bs4 import BeautifulSoup
URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
print(soup)