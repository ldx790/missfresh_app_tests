'''
@author: liudixuan
@software: SeleniumTest
@file: missfresh_my_invatation.py
@time: 2020/3/25 17:38
@desc:
'''

from pages.invite_page import InviPage
from cases.base_case import *
from conmon.logger import Logger

logger = Logger().logger

class MyInvite(BaseCase):
    '''
    邀请得现金模块
    '''

    def test_my_invite(self):
        '''
        MRYX-ST-FU-008；验证跳转邀请得现金成功
        :return:
        '''
        weixin_activity = 'com.tencent.mm.ui.transmit.SelectConversationUI'
        # 去到我的模块
        mp = MyPage(self.driver)
        # 向下滑动
        self.driver.swipe(314, 1187, 314, 227)
        #去到邀请得现金
        mp.invite_button_click()
        #立即邀请
        ip = InviPage(self.driver)
        ip.nowinvite_button_click()
        ip.weixin_click()
        #断言
        activites = self.driver.current_activity
        logger.info(activites)
        self.assertIn(activites,weixin_activity)

if __name__ == '__main__':
    unittest.main()

