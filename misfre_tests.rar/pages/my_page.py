'''
@author: liudixuan
@software: SeleniumTest
@file: my_page.py
@time: 2020/3/25 15:37
@desc:
'''
# class MyPage():
#     def :

from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class MyPage(BasePage):
    '''
    定位我的模块
    '''

    # 去到我的模块
    my_button_locator = (By.XPATH, '//android.widget.TextView[@text=\"我的\"]')

    #定位邀请得现金
    invite_button_locator = (By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]/android.widget.RelativeLayout/android.widget.ImageView')
    #定位收货地址
    add_address_locator = (By.XPATH,'')

    #定位积分商城
    shop_button_locator = (By.XPATH, '/hierarchy/android.widget.FrameLayout'
                                                        '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout')

    #点击积分商城
    def shop_locator_click(self):
        self.click(self.shop_button_locator)

    # 点击“我的”
    def my_button_click(self):
        self.click(self.my_button_locator)

    #点击邀请得现金
    def invite_button_click(self):
        self.click(self.invite_button_locator)

