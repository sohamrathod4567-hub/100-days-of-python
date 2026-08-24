import time

from selenium import webdriver
from selenium.webdriver.common.by import By

CURRENT_URL = "https://ozh.github.io/cookieclicker/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(CURRENT_URL)

# language_selection = driver.find_element(By.ID , value="langSelect-EN")
# language_selection.click()
time.sleep(5)
while True:
    clicker = driver.find_element(By.ID , value="bigCookie")
    clicker.click()




