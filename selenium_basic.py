# Import WD lib

# Create WD Chrome Object

# Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"

# Click on [Normal success message button]

# assert appeared green success message
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")

assert "Selenium" in driver.title
time.sleep(3)

elem = driver.find_element_by_css_selector("#normal-btn-success")
elem.click()

assert "Normal success message" not in driver.page_source
driver.close()