from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import logging
import sys
sys.path.insert(1, '../../cases')

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.infoPage import InfoPage

from utils.functions import UtilsFunctions

from utils.locators import Locators

class SystemProgramTestCases(unittest.TestCase):
    '''
    This code test all function in https://opensource-demo.orangehrmlive.com/
    '''

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        
    def test_1_invalid_login(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        loginPage.login("Admin", "admin1233") 
        error_message = driver.find_element_by_id("spanMessage").text
        self.assertEqual(error_message, "Invalid credentials") # check if login fialed

    def test_2_valid_login(self):
        driver = self.driver
        loginPage = LoginPage(driver)
        loginPage.login("Admin", "admin123") 

    def test_3_update_my_info(self):
        driver = self.driver
        infoPage = InfoPage(driver)
        # update user 
        infoPage.update_personal_detail()
        # # validate user update
        check_usrname_update = driver.find_element_by_id(Locators.personal_firstname_textbox_id).get_attribute('value') 
        self.assertEqual(check_usrname_update, "Fortune") # validate first name
        check_usrname_update = driver.find_element_by_id(Locators.personal_middlename_textbox_id).get_attribute('value') 
        self.assertEqual(check_usrname_update, "Mensah") # validate middle name
        check_usrname_update = driver.find_element_by_id(Locators.personal_lastname_textbox_id).get_attribute('value') 
        self.assertEqual(check_usrname_update, "Tede") # validate last name
        check_usrname_update = driver.find_element_by_id(Locators.personal_licexpdate_textbox_id).get_attribute('value') 
        self.assertEqual(check_usrname_update, "2025-10-16") # validate licexpdate

    def test_z_logout(self):
        driver = self.driver
        logoutFunction = UtilsFunctions(driver)
        logoutFunction.logout()

    @classmethod
    def tearDownClass(self):
        time.sleep(4)
        self.driver.close()
        self.driver.quit()


# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="../../cases/report")
    )


