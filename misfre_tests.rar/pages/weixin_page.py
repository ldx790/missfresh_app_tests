'''
@author: liudixuan
@software: SeleniumTest
@file: weixin_page.py
@time: 2020/3/26 11:00
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class WeixinPage(BasePage):
    '''
    定位微信邀请界面
    '''
    #定位选择
    # weixin_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"android:id/text1\"]')
    #
    # #获取选择内容
    # def get_weixin_text(self):
    #     self.get_text(self.weixin_locator)