# Import WD lib
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# Create WD Chrome Object
driver = webdriver.Chrome()


driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
time.sleep(3)

assert 'Selenium' in driver.title

elem = driver.find_element_by_css_selector('#normal-btn-success')
time.sleep(3)
elem.click()
time.sleep(3)
assert "normal success message." in driver.page_source
time.sleep(3)
driver.close()