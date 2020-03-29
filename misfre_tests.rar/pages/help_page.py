'''
@author: liudixuan
@software: SeleniumTest
@file: help_page.py
@time: 2020/3/25 23:13
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class HelPage(BasePage):
    '''
    定位帮助和服务的模块
    '''

    # 去到帮助和服务的模块
    helps_locator = (By.XPATH,'/hierarchy/android.widget.FrameLayout'
                                                 '/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[7]/android.widget.RelativeLayout/android.widget.ImageView')
    #定位投诉
    complaint_locator = (By.XPATH,
                                            '//android.widget.GridView[@resource-id=\"cn.missfresh.application:id/gv_bufete_service\"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]')

    #定位在线服务
    onlie_server_locator = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/bt_jump_wexin\"]')
    #点击在线服务
    def onlie_server_click(self):
        self.click(self.onlie_server_locator)

    #定位回答的问题

    #点击我要投诉
    def complaint_click(self):
        self.click(self.complaint_locator)

    #点击帮助和服务
    def helps_locator_click(self):
        self.click(self.helps_locator)
