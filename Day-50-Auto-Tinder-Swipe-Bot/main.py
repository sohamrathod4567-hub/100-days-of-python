from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


TIN_DOG_URL = "https://app.100daysofpython.dev/services/tindog/u/8ye0qtQBACuszCunE9TX_jRag6ud-CsM"

#This keeps our browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)