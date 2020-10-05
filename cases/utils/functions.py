import time

import sys
sys.path.insert(2, '../utils')
from values import Values

class UtilsFunctions():

    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        time.sleep(2)
        self.driver.find_element_by_id(Values.welcome_link_id).click()

    def click_logout(self):
        time.sleep(2)
        self.driver.find_element_by_link_text(Values.logout_link_linkText).click()

