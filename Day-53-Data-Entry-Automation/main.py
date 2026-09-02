from time import sleep

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

URL = "https://appbrewery.github.io/Zillow-Clone/"

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc7vMuMtdjXJAqHWnpg37f17tGHsAqk2Kvn_PnNU6qJGoiM9A/viewform?usp=publish-editor"

response = requests.get(URL)
zillow_web_page = response.text

addy = []
price = []
links = []


soup = BeautifulSoup(zillow_web_page, "html.parser")
# print(soup.prettify())

# Got all the Address
all_addresses = soup.find_all("address", attrs={"data-test": "property-card-addr"})
# print(all_addresses)

for address in all_addresses:
    addy.append(address.get_text(strip=True))

# print(addy)

# Got the Prices
all_prices = soup.find_all(    "span",
    attrs={"data-test": "property-card-price"}
)

for p in all_prices:
    price_text = p.get_text(strip=True)
    price_only = re.search(r"\$[\d,]+", price_text).group()
    # print(price_only)
    price.append(price_only)

# print(price)

# Got the Links

all_links = soup.find_all("a", attrs={"data-test": "property-card-link"})

for price_per_month in all_links:
    links.append(price_per_month.get("href"))
# print(links)

# This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)



#The Driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)

wait = WebDriverWait(driver, 2)
inputa =(By.CSS_SELECTOR, "input.whsOnd")
add = wait.until(
    ec.element_to_be_clickable(
        inputa
    )
)



sleep(1)
add.click()
add.send_keys("ELlo")
# print(add.get_attribute("outerHTML"))

price_per_month = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    )
)

price_per_month.click()
price_per_month.send_keys("wassappp")


link = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    )
)

link.click()
link.send_keys("wassappp")

submit_btn = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    )
)
submit_btn.click()