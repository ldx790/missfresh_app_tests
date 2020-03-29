'''
@author: liudixuan
@software: SeleniumTest
@file: shop_page.py
@time: 2020/3/26 9:54
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class ShopPage(BasePage):
    '''
    积分商城界面
    '''
    #定位我的积分
    points_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_my_integral\"]')

    #定位会员等级
    member_locator =(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_title_bubble\" and @text=\"Ⅲ级会员\"]')

    #获取我的积分内容
    def points_get(self):
        return self.get_text(self.points_locator)

    # 获取我的积分内容
    def member_get(self):
        return self.get_text(self.member_locator)