'''
@author: liudixuan
@software: SeleniumTest
@file: get_path.py
@time: 2020/3/26 21:16
@desc:
'''

from pathlib import Path
REMOTE_PATH = "http://localhost:4723/wd/hub" #远程连接地址
BASEPATH = Path(__file__).absolute().parent.parent #工程路径
p = Path(BASEPATH)
DATA_PATH = p.joinpath("datas")     #datas数据路径
COMMON_PATH = p.joinpath("conmon") #conmon工具路径
LOG_PATH = p.joinpath("log")        #log路径
CASE_PATH = p.joinpath("cases")     #cases用例路径
Desired_capabilities = {              #配置信息，json格式
            'platformName':'Android',       #平台名称
            'deviceName':'127.0.0.1:62025', #adb devives 列举出来的名称
            'platformVersion':'5.1.1',      #手机系统版本号
            'appPackage':'cn.missfresh.application',
            'appActivity':'cn.missfresh.module.base.main.view.MainActivity',
            'noReset':True                 #关闭提示，不重置
        }