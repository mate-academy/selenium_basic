from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html')
    driver.maximize_window()
    driver.find_element_by_css_selector('#normal-btn-success').click()
    assert "I'm a normal success message" in driver.page_source
    driver.quit()


if __name__ == "__main__":
    main()
    if SystemExit.code != 0:
        print("Test passed")
    else:
        print("Error")