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

from utils.locators import Locators

class AllFunctionsTestCases(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        

    def test_login_and_logout_valid(self):
        driver = self.driver
        # login 
        loginPage = LoginPage(driver)
        loginPage.login("Admin", "admin123") 
        # logout 
        loginPage.logout()

    def test_update_my_info(self):
        driver = self.driver
        infoPage = InfoPage(driver)
        # login 
        infoPage.login("Admin", "admin123") 
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
        # logout 
        infoPage.logout()

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


