'''
@author: liudixuan
@software: SeleniumTest
@file: base_page.py
@time: 2020/3/25 22:40
@desc:
'''
from appium.webdriver.common.mobileby import MobileBy as by
class BasePage():
    '''
    所有页面类的基类
    '''

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,lactor):
        '''
        元素查找方法
        :param lactor:
        :return:
        '''
        return self.driver.find_element(*lactor)
    def find_elements(self,lacator):
        return self.driver.find_elements(*lacator)


    def click(self,locator):
        '''
        点击
        :param locator:
        :return:
        '''
        return self.driver.find_element(*locator).click()

    def send_keys(self,locator,messg):
        '''
        输入文本信息
        :param locator:
        :param messg:
        :return:
        '''
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(messg)

    def get_text(self,locator):
        '''
        获取元素的文本信息
        :param locator:
        :return:
        '''
        return self.driver.find_element(*locator).text