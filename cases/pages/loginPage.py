import time

import sys
sys.path.insert(2, '../../cases')
from utils.locators import Locators
from utils.functions import UtilsFunctions

class LoginPage(UtilsFunctions):

    def __init__(self, driver):
        self.driver = driver

    # more function concerning thte login page goes here 