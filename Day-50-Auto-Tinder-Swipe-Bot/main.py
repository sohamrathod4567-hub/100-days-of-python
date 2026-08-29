from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

EMAIL = "rathodsoham999@gmail.com"
PASS = "123456789"
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

face_bark = wait.until(
    ec.element_to_be_clickable(
        (By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]')
    )
)

face_bark.click()

# Switch to the Face_bark popup window
sleep(2)
base_window = driver.window_handles[0]
face_bark_window = driver.window_handles[1]
driver.switch_to.window(face_bark_window)
# print(driver.title)

email_login = wait.until(
    ec.element_to_be_clickable(
        (By.ID, "email")
    )
)
email_login.send_keys(EMAIL)

pass_login = wait.until(
    ec.element_to_be_clickable(
        (By.ID, "pass")
    )
)
pass_login.send_keys(PASS)

face_bark_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button")
face_bark_btn.click()

# This right here, gets out focus to the main( base ) window.
driver.switch_to.window(base_window)


sleep(2)
location_btn = driver.find_element(By.XPATH,"/html/body/main/div/div/form/button")
location_btn.click()


notifications = driver.find_element(By.XPATH,'/html/body/main/div/div/form/button[2]')
notifications.click()
sleep(2)

cookies = driver.find_element(By.XPATH, '/html/body/main/div/div/form/button')
cookies.click()

for n in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        # Match popup is in the way — dismiss it and continue
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        # Like button not loaded yet OR all dogs have been swiped — wait and retry
        sleep(2)

driver.quit()