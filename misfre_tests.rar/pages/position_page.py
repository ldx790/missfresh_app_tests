'''
@author: liudixuan
@software: SeleniumTest
@file: position.py
@time: 2020/3/26 11:39
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class PosiPage(BasePage):
    '''
    定位收货地址页面
    '''
    # 定位下拉框
    select_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_city_name\"]')

    #点击下拉框
    def select_click(self):
        self.click(self.select_locator)

    #定位城市
    city_locator = (By.XPATH, '//android.widget.TextView[@text=\"上海市\"]')
    #点击城市
    def city_click(self):
        self.click(self.city_locator)

    # 输入小区
    house_locator = (By.XPATH,'//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/et_search_address_input\"]')

    def house_send_keys(self,house):
        self.send_keys(self.house_locator,house)

    # 确定小区
    housing_locator = (By.ID, 'cn.missfresh.application:id/tv_search_address_title')
    def housing_click(self,house):
        housi_locator = self.find_elements(self.housing_locator)
        for i in housi_locator:
            if i.get_attribute("text") == house:
                i.click()
                break
