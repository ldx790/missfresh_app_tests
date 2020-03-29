'''
@author: liudixuan
@software: SeleniumTest
@file: bill_page.py
@time: 2020/3/25 23:16
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class BillPage(BasePage):
    '''
    定位发票服务页面
    '''

    # 定位开票历史
    bill_history_locator = (
    By.XPATH, '//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_title_bar_right_txt\"]')

    # 去到发票服务模块
    bill_locator = (By.XPATH,'//android.widget.GridView[@resource-id=\"cn.missfresh.application:id/gv_bufete_service\"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]')

    #获取开票历史内容
    def bill_history_text(self):
        return self.get_text(self.bill_history_locator)

    #点击发票服务
    def bill_locator_click(self):
        self.click(self.bill_locator)