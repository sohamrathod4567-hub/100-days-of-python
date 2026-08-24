from selenium import webdriver
from selenium.webdriver.common.by import By

# keep the Chrome browser Open After program Finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
#
# price_dolla = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The Price is {price_dolla.text}.{price_cent.text}")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID,value="submit")
print(button.size)
# driver.close()
driver.quit()