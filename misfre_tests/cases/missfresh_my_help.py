'''
@author: liudixuan
@software: SeleniumTest
@file: missfresh_look_help.py
@time: 2020/3/25 16:02
@desc:
'''
from conmon.tool import *
import unittest
from time import sleep
from cases.base_case import BaseCase
from pages.help_page import HelPage
from pages.quistion_page import QusPage
from conmon.logger import Logger
import ddt

logger = Logger().logger

@ddt.ddt
class MyHelp(BaseCase):
    '''
    客服和帮助页面
    '''
    @ddt.data(*get_data_from_csv('answer_datas.csv'))
    @ddt.unpack
    def test_my_help(self,texts):
        '''
        MRYX-ST-FU-003；验证在线客服功发送问题成功
        :return:
        '''

        # 向下滑动去到帮助模块
        sleep(6)
        self.driver.swipe(314, 1187, 314, 227)
        # 去到客服和帮助
        hp = HelPage(self.driver)
        hp.helps_locator_click()
        #定位问题，点击问题查看答案
        sleep(15)
        qp = QusPage(self.driver)
        qp.questions_click(texts)
        #断言
        sleep(15)
        li = qp.answer_get(texts)
        logger.info(li)
        self.assertIn(texts,li)

if __name__ == '__main__':
    unittest.main()