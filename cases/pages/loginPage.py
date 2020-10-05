import time

import sys
sys.path.insert(2, '../../cases')
from utils.values import Values

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        time.sleep(2)
        self.driver.find_element_by_id(Values.username_textbox_id).clear()
        self.driver.find_element_by_id(Values.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        time.sleep(2)
        self.driver.find_element_by_id(Values.password_textbox_id).clear()
        self.driver.find_element_by_id(Values.password_textbox_id).send_keys(password)

    def click_login(self):
        time.sleep(1)
        self.driver.find_element_by_id(Values.login_button_id).click()

