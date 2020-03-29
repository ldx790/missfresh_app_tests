#!/usr/bin/env python
# encoding: utf-8
'''
@author: shichuguo
@software: SeleniumTest
@file: logger.py
@time: 2020/3/9 16:26
@desc:
'''
import os
import json
import threading
import logging.config
from conmon.get_path import *


class Logger(object):
	"""
	Python 的模块就是天然的单例模式，因为模块在第一次导入时，
	会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，
	而不会再次执行模块代码。
	因此，我们只需把相关的函数和数据定义在一个模块中，
	就可以获得一个单例对象了。如果我们真的想要一个单例类
	class Singleton(object):
	    def foo(self):
	        pass
	singleton = Singleton()  # 使用时候，直接导入singleton，则为单例模式
	"""
	_instance_lock = threading.Lock()

	def __init__(self, default_path="logger.json", default_level=logging.INFO):
		self.path = os.path.join(DATA_PATH,default_path)   #组装拼接放"logger.json"的路径
		self.logging = logging
		self.default_level = default_level
		self._logger_config()

	def __new__(cls, *args, **kwargs):  # 单例模式（只实例一次，只有一个log对象，不会生成多个）
		if not hasattr(Logger, "_instance"):
			with Logger._instance_lock:
				if not hasattr(Logger, "_instance"):
					Logger._instance = object.__new__(cls)
		return Logger._instance

	@property
	def logger(self):
		return self.logging

	def _logger_config(self):
		'''
		将存的路径塞进去，单独创建一个log包，取这个路径
		:return:
		'''
		if os.path.exists(self.path):
			with open(self.path, 'r') as f:
				config = json.load(f)  # config为dict类型。load方法读取内容并反序列化为dictionary
				info_filename = config.get("handlers").get("info_file_handler").get("filename")
				error_filename = config.get("handlers").get("error_file_handler").get("filename")
				config.get("handlers").get("info_file_handler")["filename"] = os.path.join(LOG_PATH,info_filename)
				#info_filename、error_filename都存在(LOG_PATH里
				config.get("handlers").get("error_file_handler")["filename"] = os.path.join(LOG_PATH,error_filename)
				self.logging.config.dictConfig(config)
		else:
			self.logging.basicConfig(level=self.default_level)

# obj1 = Logger()
# obj2 = Logger()
# print(obj1, obj2)


# def logger(default_path="logger.json", default_level=logging.INFO):
# 	'''
# 	返回日志对象，日志配置信息从logger.json中读取
# 	:return: logger
# 	:param default_path: 日志存放路径
# 	:param default_level: 默认日志级别
# 	:return:
# 	'''
# 	path = os.path.join(DATA_PATH, "logger.json")
# 	if os.path.exists(path):
# 		with open(path, 'r') as f:
# 			config = json.load(f)  # config为dict类型。load方法读取内容并反序列化为dictionary
# 			info_filename = config.get("handlers").get("info_file_handler").get("filename")
# 			error_filename = config.get("handlers").get("error_file_handler").get("filename")
# 			config.get("handlers").get("info_file_handler")["filename"] = os.path.join(LOG_PATH, info_filename)
# 			config.get("handlers").get("error_file_handler")["filename"] = os.path.join(LOG_PATH, error_filename)
# 			logging.config.dictConfig(config)
# 	else:
# 		logging.basicConfig(level=default_level)
# 	return logging
