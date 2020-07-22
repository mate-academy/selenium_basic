# Import WD lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Create WD Chrome Object
driver = webdriver.Chrome()
# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
time.sleep(2)
# Click on [Normal success message button]
elem = driver.find_element_by_css_selector("#normal-btn-success")
elem.click()
time.sleep(2)
# assert appeared green success message
driver.close()
