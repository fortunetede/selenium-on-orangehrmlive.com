import time
import logging
import sys
sys.path.insert(2, '../../cases')
sys.path.insert(3, '../pages')


from selenium.webdriver.support.ui import Select

from utils.locators import Locators
from utils.functions import UtilsFunctions
from pages.loginPage import LoginPage

class InfoPage(LoginPage, UtilsFunctions):

    def __init__(self, driver):
        self.driver = driver


    def update_personal_detail(self):
        log = logging.getLogger("TestLog")
        log.debug("debug message")

        driver = self.driver
        time.sleep(2)
        
        driver.find_element_by_id(Locators.my_info_link_id).click()
        time.sleep(1)
        driver.find_element_by_id(Locators.save_button_id).click()
        time.sleep(1)
        driver.find_element_by_id(Locators.personal_firstname_textbox_id).clear()
        driver.find_element_by_id(Locators.personal_firstname_textbox_id).send_keys("Fortune")
        time.sleep(1)
        driver.find_element_by_id(Locators.personal_middlename_textbox_id).clear()
        driver.find_element_by_id(Locators.personal_middlename_textbox_id).send_keys("Mensah")
        time.sleep(1)
        driver.find_element_by_id(Locators.personal_lastname_textbox_id).clear()
        driver.find_element_by_id(Locators.personal_lastname_textbox_id).send_keys("Tede")
        time.sleep(1)
        driver.find_element_by_id(Locators.personal_licexpdate_textbox_id).clear()
        driver.find_element_by_id(Locators.personal_licexpdate_textbox_id).send_keys("2025-10-16")
        time.sleep(1)
        select_element = Select(driver.find_element_by_id(Locators.personal_marital_selectbox_id)).select_by_value("Single")
        time.sleep(1)
        driver.find_element_by_id(Locators.save_button_id).click()

        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.forward()

        
        
        

        
        


        
        
