from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


TIN_DOG_URL = "https://app.100daysofpython.dev/services/tindog/u/8ye0qtQBACuszCunE9TX_jRag6ud-CsM"

#This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#The Driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(TIN_DOG_URL)

wait = WebDriverWait(driver, 2)

log_in_btn = driver.find_element(By.XPATH , "/html/body/header/button")
log_in_btn.click()

wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]')))

face_bark = driver.find_element(By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]')
face_bark.click()