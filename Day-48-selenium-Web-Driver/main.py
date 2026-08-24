
from selenium import webdriver

# keep the Chrome browser Open After program Finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# driver.close()
# driver.quit()