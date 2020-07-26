from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
elem = driver.find_element_by_id("normal-btn-success")
elem.click()
assert "Succsess message" in driver.page_source()
driver.close()
