from time import sleep, time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://appbrewery.github.io/Zillow-Clone/"

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc7vMuMtdjXJAqHWnpg37f17tGHsAqk2Kvn_PnNU6qJGoiM9A/viewform?usp=publish-editor"

response = requests.get(URL)
zillow_web_page = response.text

addy = []
prices = []
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
    prices.append(price_only)

# print(price)

# Got the Links

all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

all_links = soup.find_all("a", attrs={"data-test": "property-card-link"})

for price_per_month in all_links:
    links.append(price_per_month.get("href"))
# print(links)

# This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)



#The Driver
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 2)
for n in range(len(all_links)):
    # TODO: Add fill in the link to your own Google From
    driver.get(FORM_URL)

    # Use the xpath to select the "short answer" fields in your Google Form.
    # Note, your xpath might be different if you created a different form.
    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(addy[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit_button.click()
