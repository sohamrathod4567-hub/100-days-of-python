from pandas.core.indexing import check_dict_or_set_indexers
from selenium import webdriver

# keep the Chrome browser Open After program Finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")