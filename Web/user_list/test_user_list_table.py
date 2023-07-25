import unittest
import time
import HTMLTestRunner
import random

import user_list_page_locators
import user_generator

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "https://www.way2automation.com/angularjs-protractor/webtables/"
driver = webdriver.Chrome()


class TestUserListTable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.locators = user_list_page_locators.UserListPageLocators()
        cls.user = user_generator.UserGenerator()
        cls.unique_username = None

    def test_01_navigate_to_user_list_table(self):
        print("Navigating to user list table")

        #   we validate that we are on the correct url
        driver.get(url)
        current_url = driver.current_url

        self.assertEqual(url, current_url, "ERROR: Incorrect URL!")
        time.sleep(5)

    def test_02_click_add_user_button(self):
        print("Click on Add User button")

        button = driver.find_element(By.XPATH, self.locators.add_user_button)
        button.click()

    def test_03_add_user_to_user_list(self):
        print("Adding user to table")

        user = self.user.generate_user_details()

        # adding random choice for customer type
        customer_types = random.choice([user_list_page_locators.UserListPageLocators.customer_radio_btn1,
                                        user_list_page_locators.UserListPageLocators.customer_radio_btn2])

        # adding random choice for role type using index
        customer_role_types = random.choice([1, 2, 3])

        # input first name
        fname_box = driver.find_element(By.XPATH, self.locators.first_name)
        fname_box.send_keys(user['first_name'])

        # input last name
        lname_box = driver.find_element(By.XPATH, self.locators.last_name)
        lname_box.send_keys(user['last_name'])

        # input username
        uname_box = driver.find_element(By.XPATH, self.locators.user_name)
        uname_box.send_keys(user['username'])
        self.__class__.unique_username = user['username']

        # input password
        uname_box = driver.find_element(By.XPATH, self.locators.password)
        uname_box.send_keys(user['password'])

        # choose customer type
        customer_type = driver.find_element(By.XPATH, customer_types)
        customer_type.click()

        # choose role type
        customer_role = Select(driver.find_element(By.XPATH, self.locators.customer_role_box))
        customer_role.select_by_index(str(customer_role_types))

        # input email
        email_box = driver.find_element(By.XPATH, self.locators.customer_email)
        email_box.send_keys(user['email'])

        # input cellphone
        cell_box = driver.find_element(By.XPATH, self.locators.customer_cell)
        cell_box.send_keys(user['cell'])

        # save user
        save_btn = driver.find_element(By.XPATH, self.locators.save_button)
        save_btn.click()

    def test_04_user_exists_in_list(self):
        print("Validating user exists in user list")

        self.assertTrue(self.unique_username in driver.page_source, f"ERROR: Could not find {self.unique_username} "
                                                                    f"in user list!")

    @classmethod
    def tearDownClass(cls):
        print("All tests completed - close browsers")
        driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()









