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
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        

    def test_login_and_logout_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        # login 
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()  
        # logout 
        logout = HomePage(driver)
        logout.click_welcome()
        logout.click_logout()

    def test_update_my_info(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        # login 
        info = InfoPage(driver)
        info.enter_username("Admin")
        info.enter_password("admin123")
        info.click_login()  
        # update user 
        info.update_personal_detail()
        # logout 
        info.click_welcome()
        info.click_logout()

    @classmethod
    def tearDownClass(cls):
        time.sleep(4)
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="../../cases/report")
    )


