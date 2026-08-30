from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

X_URL = "https://x.com/home"

#This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)