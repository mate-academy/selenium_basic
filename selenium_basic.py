# Import WD lib
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Create WD Chrome Object
driver = webdriver.Chrome()
# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
time.sleep(2)
# Click on [Normal success message button]
driver.find_element_by_css_selector("#normal-btn-success").click()
time.sleep(2)
assert "I'm a normal success message." in driver.page_source
time.sleep(2)
driver.quit()
