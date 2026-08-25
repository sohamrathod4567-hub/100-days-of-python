import os
from selenium import webdriver
from selenium.webdriver.common.by import By

ACCOUNT_EMAIL= "rathodsoham999@gmail.com"
ACCOUNT_PASSWORD ="9879915801"
GYM_URL ="https://appbrewery.github.io/gym/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

login_email = driver.find_element(By.NAME, "email")
login_email.send_keys(ACCOUNT_EMAIL)

login_password = driver.find_element(By.NAME, "password")
login_password.send_keys(ACCOUNT_PASSWORD)

submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()