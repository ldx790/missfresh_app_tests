'''
@author: liudixuan
@software: SeleniumTest
@file: misssfresh_my_complaint.py
@time: 2020/3/25 16:27
@desc:
'''
from conmon.tool import *
from appium.webdriver.common.mobileby import MobileBy as By
import unittest

from pages.help_page import HelPage
from pages.server_page import SerPage
from cases.base_case import *
from time import sleep
from conmon.logger import Logger

logger = Logger().logger
class MyComp(BaseCase):
    '''
    我要投诉功能
    '''

    def test_my_complain(self):
        '''
        MRYX-ST-FU-010；验证自助服务_成功跳转我要投诉界面
        :return:
        '''
        # 向下滑动去到帮助模块
        # swipeDown(driver,1000)
        self.driver.swipe(314, 1187, 314, 227)
        # 去到客服和帮助
        hp = HelPage(self.driver)
        hp.helps_locator_click()
        #去到我要投诉页面
        hp.complaint_click()
        #定位在线客服问题发送框
        sp = SerPage(self.driver)
        sp.get_answer_send_keys("3")
        #发送信息
        sp.send_click()
        #断言
        sleep(6)
        text = sp.my_answer_get(num=3)
        logger.info(text)
        self.assertIn("3", text)
