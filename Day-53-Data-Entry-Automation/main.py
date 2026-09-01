import requests
from selenium import webdriver
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc7vMuMtdjXJAqHWnpg37f17tGHsAqk2Kvn_PnNU6qJGoiM9A/viewform?usp=publish-editor"

response = requests.get(URL)
zillow_web_page = response.text


soup = BeautifulSoup(zillow_web_page, "html.parser")
# print(soup.prettify())
address = soup.find_all(name = "a",class_= "StyledPropertyCardDataArea-anchor")