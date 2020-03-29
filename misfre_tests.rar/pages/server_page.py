'''
@author: liudixuan
@software: SeleniumTest
@file: server_page.py
@time: 2020/3/26 10:07
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class SerPage(BasePage):
    '''
    定位在线客服页面
    '''

    # 定位在线客服问题发送框
    get_answer_locator =(By.XPATH,'//android.widget.EditText[@resource-id=\"cn.missfresh.application:id/sobot_et_sendmessage\"]/child::android.widget.RelativeLayout/android.widget.LinearLayout')

    #定位发送按钮
    send_locator = (By.XPATH, '/hierarchy/android.widget.'
                                                 'FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button')





    #获取我的回答的内容

    def my_answer_get(self,num):
        # l = self.find_elements(self.my_answer_locator)
        # li = []
        # for i in l:
        #     text = i.text
        #     li.append(text)
        # return li
        my_answer_locator = (By.XPATH, '//*[@text={}]'.format(num))  #定位我的回答
        self.get_text(my_answer_locator)


    #定位客服回答
    answer_locator = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"cn.missfresh.application:id/sobot_real_ll_content\"]')

    #获取客服回答内容
    # def get_answer_text(self):





    #点击发送
    def send_click(self):
        self.click(self.send_locator)

    #输送咨询消息
    def get_answer_send_keys(self,messg):
        self.send_keys(self.get_answer_locator,messg)