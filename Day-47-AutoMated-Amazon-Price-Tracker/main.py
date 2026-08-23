import requests
from bs4 import BeautifulSoup
URL = "https://appbrewery.github.io/instant_pot/"

response = requests.get(URL)
product_web_page = response.text
soup = BeautifulSoup(product_web_page, "html.parser")
# print(soup)
price = soup.find(name="span", class_="a-price-whole").get_text(strip=True)
price = float(price.replace(".", ""))
print(price)