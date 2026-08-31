import time
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




class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.get(LOGIN_URL)


    def login(self):

        first_login_btn = self.driver.find_element(By.XPATH, "/html/body/div/aside/div/form/button")
        first_login_btn.click()

        username = self.driver.find_element(By.ID, 'username')
        username.send_keys(EMAIL)

        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(PASSWORD)

        login_btn = self.driver.find_element(By.XPATH, "/html/body/div/div/form/button")
        login_btn.click()
        time.sleep(2)

        not_now_btn = self.driver.find_element(By.CLASS_NAME, "naan-popup-dismiss")
        not_now_btn.click()

        no_btn = self.driver.find_element(By.XPATH, '//*[@id="popup-notifications"]/div/button[2]')
        no_btn.click()



    def find_followers(self):
        search_btn = self.driver.find_element(By.XPATH,'/html/body/div[1]/nav/button')
        search_btn.click()

        search_input = self.driver.find_element(By.CLASS_NAME, "naan-search-input")
        search_input.send_keys(SIMILAR_ACCOUNT)

    def follow(self):
        pass

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()