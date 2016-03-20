#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: folderOperate.py
@time: 2016/3/19 23:23
"""


import os
import time

# # 获取当前目录
# s = os.getcwd()
# print(s)
# # C:\Users\Dave\PycharmProjects\spiderInWeek\week2

# # 创建一个文件夹，以创建它的时间命名
# folder = time.strftime(r"%Y-%m-%d_%H-%M-%S", time.localtime())
# os.makedirs('{}/{}'.format(os.getcwd(), folder))
#
# b = os.path.exists('c:\\123')
# print(b)
import requests
imgUrl = 'http://cache.mrporter.com/images/products/676897/676897_mrp_in_l.jpg'
response = requests.get(imgUrl, stream=True)
image = response.content
brand = 'nike'
pwd = os.getcwd()
path_ = pwd + "\\" + brand + '\\'
print(path_)
filename = '1'+'.jpg'
if not os.path.exists(path_):
	os.makedirs('{}/{}'.format(os.getcwd(), brand))
	with open(path_  + filename, "wb") as img:
		img.write(image)
else:
	with open(path_  + filename, "wb") as img:
		img.write(image)
