# Import WD lib

# Create WD Chrome Object

# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"

# Click on [Normal success message button]

# assert appeared green success message

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
assert "Selenium" in driver.title
elem = driver.find_element_by_id("normal-btn-success")
elem.click()
time.sleep(5)
assert "normal success message" in driver.page_source
driver.close()