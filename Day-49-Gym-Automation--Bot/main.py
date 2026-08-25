import os
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")