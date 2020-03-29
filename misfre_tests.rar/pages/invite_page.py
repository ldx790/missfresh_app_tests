'''
@author: liudixuan
@software: SeleniumTest
@file: invite_page.py
@time: 2020/3/26 10:34
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class InviPage(BasePage):
    '''
    定位邀请有礼界面
    '''

    #定位立即邀请
    nowinvite_button_locator = (By.XPATH,
                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button')

    #定位到邀请的界面
    weixin_locator = (By.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[18]/android.view.View[2]/android.view.View[4]/android.widget.Image')

    #点击微信邀请
    def weixin_click(self):
        try:
            if self.find_element(self.weixin_locator):
                self.click(self.weixin_locator)
        except NoSuchElementException:
                pass


    #点击立即邀请
    def nowinvite_button_click(self):
        self.click(self.nowinvite_button_locator)
