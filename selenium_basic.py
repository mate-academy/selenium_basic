# Import WD lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create WD Chrome Object
driver = webdriver.Chrome()

# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")

# Click on [Normal success message button]
element = driver.find_element_by_id('normal-btn-success')
element.click()

# assert appeared green success message
assert "I'm a normal success message." in driver.page_source
driver.close()
