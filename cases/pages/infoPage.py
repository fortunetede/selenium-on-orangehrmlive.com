import time

import sys
sys.path.insert(2, '../../cases')
sys.path.insert(3, '../pages')

from utils.values import Values
from utils.functions import UtilsFunctions
from pages.loginPage import LoginPage

class InfoPage(LoginPage, UtilsFunctions):

    def __init__(self, driver):
        self.driver = driver


    def update_personal_detail(self):
        time.sleep(2)
        self.driver.find_element_by_id(Values.my_info_link_id).click()
        time.sleep(1)
        self.driver.find_element_by_id(Values.save_button_id).click()
        time.sleep(1)
        self.driver.find_element_by_id(Values.personal_firstname_textbox_id).clear()
        self.driver.find_element_by_id(Values.personal_firstname_textbox_id).send_keys("Fortune")
        time.sleep(1)
        self.driver.find_element_by_id(Values.personal_middlename_textbox_id).clear()
        self.driver.find_element_by_id(Values.personal_middlename_textbox_id).send_keys("Mensah")
        time.sleep(1)
        self.driver.find_element_by_id(Values.personal_lastname_textbox_id).clear()
        self.driver.find_element_by_id(Values.personal_lastname_textbox_id).send_keys("Tede")
        time.sleep(1)
        self.driver.find_element_by_id(Values.personal_licexpdate_textbox_id).clear()
        self.driver.find_element_by_id(Values.personal_licexpdate_textbox_id).send_keys("2025-10-16")
        time.sleep(1)
        self.driver.find_element_by_id(Values.save_button_id).click()


        
        
