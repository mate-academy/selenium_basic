from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:/selenium/chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
driver.find_element_by_id("autoclosable-btn-success").click();
alertMessage = driver.find_element_by_class_name("alert, alert-success, alert-autocloseable-success").text

assert "I'm an autocloseable success message. I will hide in 5 seconds." in alertMessage