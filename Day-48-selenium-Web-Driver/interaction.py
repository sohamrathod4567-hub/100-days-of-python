from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",value=True)

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_number = driver.find_element(By.ID, value="mwDw")
#
# print(articles_number.text)

search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search.send_keys("Python")
# driver.quit()