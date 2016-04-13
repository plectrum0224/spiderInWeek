#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: count.py
@time: 2016/3/27 13:16
"""


import pymongo
import time



while True:
	client = pymongo.MongoClient('localhost', 27017)
	GJ = client['GJ']
	itemLink = GJ['itemLink']
	productDetail = GJ['productDetail']
	print(itemLink.find().count())
	print(productDetail.find().count())
	time.sleep(5)
