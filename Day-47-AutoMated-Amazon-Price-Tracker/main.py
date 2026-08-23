import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("G_USERNAME")
MY_PASSWORD = os.getenv("G_PASSWORD")
URL = "https://www.amazon.com/dp/B01NBKTPTS?th=1"
TARGET_PRICE = 100

response = requests.get(URL)
product_web_page = response.text
soup = BeautifulSoup(product_web_page, "html.parser")
# print(soup)
price = soup.find(name="span", class_="a-price-whole").get_text(strip=True)
price = float(price.replace(".", ""))
print(price)
if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="rathodsoham999@gmail.com",
                            msg=f"Subject :Price Drop alert!\n\n Hello there , hope you are having a great day, the product which you wanted to buy from a really long time has a price drop , check it out over here {URL}"
                            )
    print("Mail sent!!")
else:
    print("The price have not met your condition")