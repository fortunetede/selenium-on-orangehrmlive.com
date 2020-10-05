from selenium import webdriver
import time
import unittest
import HtmlTestRunner

import sys
sys.path.insert(1, '../../cases')

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.infoPage import InfoPage

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
        driver.back()
        # logout 
        infoPage.logout()

    @classmethod
    def tearDownClass(self):
        time.sleep(4)
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="../../cases/report")
    )


