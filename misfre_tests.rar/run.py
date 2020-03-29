'''
@author: liudixuan
@software: SeleniumTest
@file: run.py
@time: 2020/3/26 21:24
@desc:
'''
import unittest
from conmon.get_path import *
import time
from BeautifulReport import BeautifulReport
from conmon.logger import Logger
import unittest
from conmon.get_path import *
logger = Logger().logger


discover = unittest.defaultTestLoader.discover(CASE_PATH,pattern="missfresh_my_*.py")
_time = time.strftime("%Y-%m-%d %H_%M_%S")
filename = "missfresh_{}.html".format(_time)
logger.info(filename)
BeautifulReport(discover).report(description='missfresh-tests',report_dir='report',filename=filename)