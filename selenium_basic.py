from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
norm_bton = driver.find_element_by_id("normal-btn-success")
norm_bton.click()
assert "success message" in driver.page_source
driver.close()