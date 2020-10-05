import time

import sys
sys.path.insert(2, '../utils')
from locators import Locators

class UtilsFunctions():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # enter username 
        time.sleep(2)
        self.driver.find_element_by_id(Locators.username_textbox_id).clear()
        self.driver.find_element_by_id(Locators.username_textbox_id).send_keys(username)
        # enter password 
        time.sleep(2)
        self.driver.find_element_by_id(Locators.password_textbox_id).clear()
        self.driver.find_element_by_id(Locators.password_textbox_id).send_keys(password)
        # click login 
        time.sleep(1)
        self.driver.find_element_by_id(Locators.login_button_id).click()
        
    def logout(self):
        time.sleep(2)
        self.driver.find_element_by_id(Locators.welcome_link_id).click()
        time.sleep(2)
        self.driver.find_element_by_link_text(Locators.logout_link_linkText).click()

    

