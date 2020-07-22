# Import WD lib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Create WD Chrome Object
driver = webdriver.Chrome()
# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
# Click on [Normal success message button]
normal_btn = driver.find_element_by_id('normal-btn-success')
normal_btn.click()
# assert appeared green success message
assert "I'm a normal success message." in driver.page_source
driver.close()