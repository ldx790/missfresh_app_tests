'''
@author: liudixuan
@software: SeleniumTest
@file: tool.py
@time: 2020/3/24 18:33
@desc:
'''
from appium import webdriver
import csv
import os
from conmon.get_path import *


# 获得机器屏幕大小x,y
def getSize(dr):
	x = dr.get_window_size()['width']
	y = dr.get_window_size()['height']
	return (x, y)  #(720,1280)


# 屏幕向上滑动
def swipeUp(dr, t):
	l = getSize(dr) #(720,1280)
	x1 = int(l[0] * 0.5)  # x坐标  360
	y1 = int(l[1] * 0.75)  # 起始y坐标  960
	y2 = int(l[1] * 0.25)  # 终点y坐标  320
	dr.swipe(x1, y1, x1, y2, t)


# 屏幕向下滑动
def swipeDown(dr, t):
	l = getSize(dr)
	x1 = int(l[0] * 0.5)  # x坐标
	y1 = int(l[1] * 0.25)  # 起始y坐标  320
	y2 = int(l[1] * 0.75)  # 终点y坐标  960
	dr.swipe(x1, y1, x1, y2, t)


# 屏幕向左滑动
def swipLeft(dr, t):
	l = getSize(dr)
	x1 = int(l[0] * 0.75)
	y1 = int(l[1] * 0.5)
	x2 = int(l[0] * 0.05)
	dr.swipe(x1, y1, x2, y1, t)


# 屏幕向右滑动
def swipRight(dr, t):
	l = getSize(dr)
	x1 = int(l[0] * 0.05)
	y1 = int(l[1] * 0.5)
	x2 = int(l[0] * 0.75)
	dr.swipe(x1, y1, x2, y1, t)


# 屏幕快速向右滑动
def flickSwipRight(dr):
	l = getSize(dr)
	x1 = int(l[0] * 0.05)
	y1 = int(l[1] * 0.5)
	x2 = int(l[0] * 0.75)
	dr.flick(x1, y1, x2, y1)

#获取元素
def get_data_from_csv(filename):
	file_name = os.path.join(DATA_PATH,filename)
	with open(file_name,'r',encoding='utf-8') as f:
		data = csv.reader(f)
		datas = []
		for i in data:
			datas.append(tuple(i))
		return datas[1:]
