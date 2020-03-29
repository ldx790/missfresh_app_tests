'''
@author: liudixuan
@software: SeleniumTest
@file: missfresh_check_shop.py
@time: 2020/3/25 15:32
@desc:
'''
import unittest
from conmon.tool import *
from pages.my_page import MyPage
from cases.base_case import BaseCase
from time import sleep
from pages.shop_page import ShopPage
from conmon.logger import Logger

logger = Logger().logger

class MyShop(BaseCase):
    '''
    积分商城模块
    '''

    def test_my_shop(self):
        '''
        MRYX-ST-FU-001；验证查看积分商城
        :return:
        '''
        # 去到我的模块
        mp = MyPage(self.driver)
        # 向下滑动去到帮助模块
        self.driver.swipe(314,1187,314,227)
        # 去到积分商城
        mp.shop_locator_click()
        #向下滑动
        sp = ShopPage(self.driver)
        sleep(5)
        swipeDown(self.driver,1000)
        # 断言
        text = sp.points_get()
        logger(text)
        self.assertIn("我的积分",text)
        sleep(6)
        #向上滑动
        swipeUp(self.driver,1000)
        sleep(6)
        # 断言
        texts = sp.member_get()
        logger.info(texts)
        self.assertIn("Ⅲ级会员", texts)






