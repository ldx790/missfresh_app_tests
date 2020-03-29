'''
@author: liudixuan
@software: SeleniumTest
@file: missfresh_my_bill.py
@time: 2020/3/25 16:31
@desc:
'''

from conmon.tool import *
from appium.webdriver.common.mobileby import MobileBy as By
import unittest
from conmon.tool import *
from cases.base_case import BaseCase
from pages.my_page import MyPage
from pages.help_page import HelPage
from pages.bill_page import BillPage
from time import sleep
from conmon.logger import Logger

logger = Logger().logger

class Mybill(BaseCase):
    '''
    发票服务模块
    '''
    def test_my_bill(self):
        '''
        MRYX-ST-FU-009;查验我的发票服务成功跳转并显示内容
        :return:
        '''
        #向下滑动去到帮助模块
        sleep(10)
        self.driver.swipe(314,1187,314,227)
        #去到客服和帮助
        sleep(10)
        hp = HelPage(self.driver)
        hp.helps_locator_click()
        #去到发票服务页面
        sleep(10)
        bp = BillPage(self.driver)
        bp.bill_locator_click()
        #断言
        sleep(10)
        text = bp.bill_history_text()
        logger.info(text)
        self.assertIn('开票历史',text)

