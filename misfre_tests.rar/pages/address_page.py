'''
@author: liudixuan
@software: SeleniumTest
@file: address_page.py
@time: 2020/3/26 11:39
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class AddresPage(BasePage):
    '''
    添加地址页面
    '''
    # 定位收获地址
    address_button_locator = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.RelativeLayout/android.widget.ImageView')

    # 输入手机定位
    phone_locator = (By.XPATH,'//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/et_edit_address_tel\"]')

    # 定位新增货获地址
    add_address_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_btn_text\"]')

    #点击新增收货地址
    def add_address_click(self):
        self.click(self.add_address_locator)

    # 收货人定位
    consigneer_locator = (By.XPATH,'//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/et_edit_address_receiver\"]')


    # 定位性别定位
    gender_locator = (By.XPATH,'//android.widget.RadioButton[@resource-id=\"cn.missfresh.application:id/rg_sex_lady\"]')

    # 点击收货人
    def consigneer_send_keys(self, consigneer):
        self.send_keys(self.consigneer_locator, consigneer)

    #点击性别
    def gender_click(self):
        self.click(self.gender_locator)

    # 点击收获地址
    def address_button_click(self):
        self.click(self.address_button_locator)

    # 输入手机
    def phone_send_keys(self,phone):
        self.send_keys(self.phone_locator,phone)

    # 定位添加的地址
    my_address_locator = (
    By.XPATH, '//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_address_detail\"]')

    #定位家标签
    tag_locator = (By.XPATH,'//android.widget.RadioButton[@resource-id=\"cn.missfresh.application:id/rb_home_address_tags\"]')

    #定位保存收货地址
    save_adress_locator = (By.XPATH,'//android.widget.Button[@resource-id=\"cn.missfresh.application:id/btn_save_address\"]')

    # 定位门牌号
    roomnum_locator = (
    By.XPATH, '//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/et_edit_doorplate\"]')

    #去到定位页面
    position_locator = (By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_edit_detail_address\"]')

    # 点击家标签
    def tag_click(self):
        self.click(self.tag_locator)

    #点击定位
    def position_click(self):
        self.click(self.position_locator)

    #获取我的地址的内容
    def my_address_get(self):
        return self.get_text(self.my_address_locator)


    # 输入门牌号
    def roomnum_send_keys(self, roomnum):
        self.send_keys(self.roomnum_locator, roomnum)

    #点击保存收货地址
    def save_adress_click(self):
        self.click(self.save_adress_locator)