from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",value=True)

driver = webdriver.Chrome()
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

# articles_number = driver.find_element(By.ID, value="mwDw")
#
# print(articles_number.text)
#
# search = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
# search.send_keys("Python")

fname = driver.find_element(By.NAME,"fName")
lname = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")

fname.send_keys("Soham")
lname.send_keys("Rathod")
email.send_keys("popliboy@gmail.com")

sign_up = driver.find_element(By.CSS_SELECTOR,"form button")
sign_up.click()

# driver.quit()