from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

ACCOUNT_EMAIL= "rathodsoham999@gmail.com"      #Credentials which are used to log in to the gym page.
ACCOUNT_PASSWORD ="9879915801"
GYM_URL ="https://appbrewery.github.io/gym/"  #The actual Gym URL( it is a static website for practice purposes

#This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#From here, your chrome profile gets saved in your file path
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

#The Driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

login_email = driver.find_element(By.NAME, "email")
login_email.send_keys(ACCOUNT_EMAIL)

login_password = driver.find_element(By.NAME, "password")
login_password.send_keys(ACCOUNT_PASSWORD)

submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

class_cards = driver.find_elements(By.CSS_SELECTOR,"div[id^='class-card-']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]" )
    day_title = day_group.find_element(By.TAG_NAME , "h2").text

    if "Tue" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text