import time

import sys
sys.path.insert(2, '../../cases')
from utils.values import Values

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        time.sleep(2)
        self.driver.find_element_by_id(Values.welcome_link_id).click()

    def click_logout(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(Values.logout_link_linkText).click()

