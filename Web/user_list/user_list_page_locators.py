from selenium.webdriver.common.by import By
from selenium import webdriver


class UserListPageLocators(object):
    add_user_button = "//button[contains(text(), 'Add User')]"
    first_name = "/html/body/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input"
    last_name = "/html/body/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/input"
    user_name = "/html/body/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input"
    password = "/html/body/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input"
    customer_radio_btn1 = "/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/label[1]/input"
    customer_radio_btn2 = "/html/body/div[2]/div[2]/form/table/tbody/tr[5]/td[2]/label[2]/input"
    customer_role_box = "/html/body/div[2]/div[2]/form/table/tbody/tr[6]/td[2]/select"
    customer_email = "/html/body/div[2]/div[2]/form/table/tbody/tr[7]/td[2]/input"
    customer_cell = "/html/body/div[2]/div[2]/form/table/tbody/tr[8]/td[2]/input"
    save_button = "/html/body/div[2]/div[3]/button[2]"
