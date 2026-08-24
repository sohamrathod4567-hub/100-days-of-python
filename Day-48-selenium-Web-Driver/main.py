from selenium import webdriver
from selenium.webdriver.common.by import By

# keep the Chrome browser Open After program Finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/instant_pot/")

price_dolla = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The Price is {price_dolla.text}.{price_cent.text}")


# driver.close()
driver.quit()