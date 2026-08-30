from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

Y_URL = "https://app.100daysofpython.dev/services/y/home"
Y_EMAIL = "rathodsoham999@gmail.com"
Y_PASSWORD = "QMCz_l_-vB3xnhJi"

#This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#The Driver
driver = webdriver.Chrome(options=chrome_options)
driver.get(Y_URL)

wait = WebDriverWait(driver, 2)

y_sign_in_btn = wait.until(
  ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div/p[2]/a')
    )
)
y_sign_in_btn.click()

email = driver.find_element(By.NAME , "email")
email.send_keys(Y_EMAIL)

password = driver.find_element(By.NAME , "password")
password.send_keys(Y_PASSWORD)

sign_in = driver.find_element(By.XPATH, "/html/body/div/div/form/button")
sign_in.click()

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()