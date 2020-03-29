'''
@author: liudixuan
@software: SeleniumTest
@file: missfresh_my_server.py
@time: 2020/3/25 16:23
@desc:
'''

from pages.help_page import HelPage
from pages.server_page import SerPage
from cases.base_case import *
from time import sleep
from conmon.logger import Logger

logger = Logger().logger

class MySever(BaseCase):
    '''
    在线客服模块
    '''

    def test_my_server(self):
        '''
        MRYX-ST-FU-003；验证在线客服功发送问题成功
        :return:
        '''
        # 向下滑动去到帮助模块
        sleep(10)
        self.driver.swipe(314, 1187, 314, 227)
        # 去到客服和帮助
        hp = HelPage(self.driver)
        hp.helps_locator_click()
        #点击在线服务
        hp.onlie_server_click()
        #定位在线客服问题发送框
        sp = SerPage(self.driver)
        sleep(10)
        sp.get_answer_send_keys("4")
        #发送信息
        sp.send_click()
        #断言
        sleep(6)
        text = sp.my_answer_get(num=4)
        logger.info(text)
        self.assertIn("4",text)


if __name__ == '__main__':
    unittest.main()


