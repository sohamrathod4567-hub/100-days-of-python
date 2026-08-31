from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait



EMAIL = "rathodsoham999@gmail.com"
PASSWORD = "Z0ZINta5FXA38ihg"
SIMILAR_ACCOUNT = "rordongamsay"
LOGIN_URL = "https://app.100daysofpython.dev/services/share-a-naan/welcome"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(LOGIN_URL)

login_btn = driver.find_element(By.XPATH, "/html/body/div/aside/div/form/button")
login_btn.click()

username = driver.find_element(By.ID, 'username')
username.send_keys(EMAIL)

password = driver.find_element(By.ID, 'password')
password.send_keys(PASSWORD)