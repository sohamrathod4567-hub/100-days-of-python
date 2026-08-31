import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException



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
        self.wait = WebDriverWait(self.driver, 2)


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

        person_profile =self.wait.until(
     ec.element_to_be_clickable(
        (By.XPATH, '/html/body/aside/div[4]/a')
         )
         )

        person_profile.click()

    def follow(self):
        followers = self.driver.find_element(By.XPATH, ' /html/body/div[1]/main/header/div[2]/div[2]/span[2]/a')
        followers.click()

        list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for follow  in list_of_followers:
            try:
                follow.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                    cancel_btn = self.driver.find_element(By.XPATH , '/html/body/div[6]/div/button[2]')
                    cancel_btn.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()