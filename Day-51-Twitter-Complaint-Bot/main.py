from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

Y_URL = "https://app.100daysofpython.dev/services/y/home"
Y_EMAIL = "rathodsoham999@gmail.com"
Y_PASSWORD = "QMCz_l_-vB3xnhJi"
SPEED_TEST_URL = "https://www.speedtest.net/"
PROMISED_UP = 50
PROMISED_DOWN = 50

#This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)



class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")


        time.sleep(3)

        go_button = self.driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button')
        go_button.click()

        continue_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        continue_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3').text
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="root"]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3').text
        print(f"Your Down speed is :{self.down}")
        print(f"Your Up Speed is :{self.up}")
    def tweet_at_provider(self):
        # The Driver
        self.driver.get(Y_URL)

        wait = WebDriverWait(self.driver, 2)

        y_sign_in_btn = wait.until(
          ec.element_to_be_clickable(
                (By.XPATH, '/html/body/div/p[2]/a')
            )
        )
        y_sign_in_btn.click()

        email = self.driver.find_element(By.NAME , "email")
        email.send_keys(Y_EMAIL)

        password = self.driver.find_element(By.NAME , "password")
        password.send_keys(Y_PASSWORD)

        sign_in = self.driver.find_element(By.XPATH, "/html/body/div/div/form/button")
        sign_in.click()

        content = wait.until(
            ec.element_to_be_clickable(
                (By.XPATH,'//*[@id="tweet-compose"]')
            )
        )
        content.send_keys(f"I am Currently facing issues with my Wi-Fi, my provider said that I am gurenteed to have Up:{PROMISED_UP} and Down:{PROMISED_DOWN}, But as of right now I am having Up:{self.up} and {self.down}. Please do something about it.")

        post = self.driver.find_element(By.ID, "post-btn")
        post.click()
        time.sleep(60)





bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()