

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
time.sleep(5)
assert "Selenium" in driver.title
element = driver.find_element_by_css_selector("#normal-btn-success")
element.click()
assert "normal success message" in driver.page_source
driver.close()
print("[Normal success message] button is on page")
