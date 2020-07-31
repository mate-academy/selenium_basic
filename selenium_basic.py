# Import WD lib

# Create WD Chrome Object

# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"

# Click on [Normal success message button]

# assert appeared green success message
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html')
norm_successes_msg_btn = driver.find_element_by_css_selector('[id="normal-btn-success"]')
norm_successes_msg_btn.click()
assert 'success message' in driver.page_source
driver.close()