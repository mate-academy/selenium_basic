# Import WD lib
from selenium import webdriver
# Create WD Chrome Object
driver = webdriver.Chrome()
# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
# Click on [Normal success message button]
driver.find_element_by_css_selector("#normal-btn-success").click()
# assert appeared green success message
assert "success message" in driver.page_source