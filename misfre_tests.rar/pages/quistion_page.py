'''
@author: liudixuan
@software: SeleniumTest
@file: quistion_page.py
@time: 2020/3/26 9:41
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as By
from pages.base_page import BasePage

class QusPage(BasePage):
    '''
    定位帮助和服务的模块
    '''

    # 定位所有问题
    questions_locator = (By.ID, 'cn.missfresh.application:id/tv_question')

    # answer_locator=(By.XPATH,'//android.widget.TextView[@resource-id=\"cn.missfresh.application:id/tv_answer\"]')
    #点击问题
    def questions_click(self,texts):
        questions = self.find_elements(self.questions_locator)
        for i in questions:
            if i.get_attribute('text') in texts:
                i.click()
                break
    #获得问题答案
    def answer_get(self,texts):
        questions = self.find_elements(self.questions_locator)
        for i in questions:
            if i.get_attribute('text') in texts:
                answer_locator = i.find_element_by_xpath('/following-sibling::android.widget.RelativeLayout')
                return self.get_text(answer_locator)

    # def five_answer_get(self):
    #         return self.get_text(self.answer_locator)



