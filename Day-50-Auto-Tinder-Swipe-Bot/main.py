from appier import PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

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
time.sleep(2)
base_window = driver.window_handles[0]
face_bark_window = driver.window_handles[1]
driver.switch_to.window(face_bark_window)
print(driver.title)

# email_login = wait.until(
#     ec.element_to_be_clickable(
#         (By.ID, "email")
#     )
# )
# email_login.send_keys(EMAIL)
