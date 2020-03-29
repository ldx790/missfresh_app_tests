'''
@author: liudixuan
@software: SeleniumTest
@file: base_case.py
@time: 2020/3/25 15:26
@desc:
'''
from conmon.tool import *
import unittest
from conmon.get_path import *
from pages.my_page import *
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Remote(REMOTE_PATH,Desired_capabilities)
        self.driver.implicitly_wait(15)
        mp = MyPage(self.driver)
        mp.my_button_click()    #开始去到我的模块
    def tearDown(self):
        return  self.driver.quit()
        # self.driver.press_keycode(4)
        # sleep(10)
        # try:
        #     self.driver.press_keycode(4)     #返回
        # except NoSuchElementException:
        #     pass