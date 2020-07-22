# Import WD lib
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create WD Chrome Object


class SeleniumFirstTest(unittest.TestCase):

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver = webdriver.Chrome()

    def test_find_green_message(self):
        # Open "https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html"
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
        element = driver.find_element_by_id('normal-btn-success')

        # Click on [Normal success message button]
        element.click()
        # assert appeared green success message
        appeared_elem = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]')
        # print(appeared_elem.get_attribute('style'))
        # assert appeared_elem.get_attribute('style') == "display: block;"
        assert appeared_elem.is_displayed()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
