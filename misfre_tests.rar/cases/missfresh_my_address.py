'''
@author: liudixuan
@software: SeleniumTest
@file: missfresh_my_address.py
@time: 2020/3/25 17:52
@desc:
'''

import unittest
from cases.base_case import BaseCase
from pages.address_page import AddresPage
from pages.position_page import PosiPage
from time import sleep
import ddt
from conmon.tool import *
from conmon.logger import Logger

logger = Logger().logger
@ddt.ddt
class MyAress(BaseCase):
    '''
    收货地址模块
    '''

    @ddt.data(*get_data_from_csv('add_adress_datas.csv'))
    @ddt.unpack
    def test_my_adress(self,consigneer,phone,house,roomnum):
        '''
        MRYX-ST-FU-007;验证收货地址成功_所有项输入合法
        :return:
        '''
        # 向下滑动去到帮助模块
        self.driver.swipe(314, 1187, 314, 227)
        #去到收获地址
        sleep(7)
        ap = AddresPage(self.driver)
        ap.address_button_click()
        sleep(5)
        #去到新增收获地址
        ap.add_address_click()
        #收货人定位
        sleep(5)
        ap.consigneer_send_keys(consigneer)
        #性别定位
        ap.gender_click()
        #输入手机定位
        sleep(8)
        ap.phone_send_keys(phone)
        #去到定位页面
        sleep(7)
        ap.position_click()
        #在定位页面
        pp = PosiPage(self.driver)
        #定位市
        sleep(15)
        pp.select_click()
        pp.city_click()
        #输入小区
        sleep(10)
        pp.house_send_keys(house)
        #确定小区
        pp.housing_click(house)
        #门牌号
        sleep(10)
        ap.roomnum_send_keys(roomnum)
        #标签
        sleep(10)
        ap.tag_click()
        sleep(10)
        #保存收货地址
        ap.save_adress_click()
        #断言
        sleep(10)
        text = ap.my_address_get()
        logger.info(text)
        self.assertIn(house,text)






