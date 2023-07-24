import unittest
import time
import user_list_page_locators
import HTMLTestRunner

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.way2automation.com/angularjs-protractor/webtables/"


class TestUserListTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.locators = user_list_page_locators.UserListPageLocators()

    # def setUp(self):
    #     self.driver = webdriver.Chrome()

    def test_01_navigate_to_user_list_table(self):
        print("Navigating to user list table")

        #   we validate that we are on the correct url
        driver = self.driver
        driver.get(url)
        current_url = driver.current_url

        self.assertEqual(url, current_url, "ERROR: Incorrect URL!")
        time.sleep(5)

    def test_02_add_user(self):
        print("Adding user")

        driver = self.driver
        button = driver.find_element(By.XPATH, self.locators.add_user_button)
        button.click()
        time.sleep(5)

    #  TODO: fix teardown
    # @classmethod
    # def tearDownClass(cls):
    #     print("All tests completed - close browsers")
    #     webdriver.Chrome.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()









