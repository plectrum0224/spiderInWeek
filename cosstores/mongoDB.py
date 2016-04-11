#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: mongoDB.py
@time: 2016/3/23 23:34
"""

import pymongo
# 将链接存放到数据库中，传入两个参数， 分别是表的名称，插入数据
def saveToDB(tableName, dataDict):
	client = pymongo.MongoClient('localhost', 27017)
	cosstores = client['cosstores']
	tab = cosstores[tableName]
	for item in dataDict:
		tab.insert_one(item)
		print("插入数据成功")
	print('Done')
# 按照表的名称查找此表中所有数据
def findLink(tableName):
	client = pymongo.MongoClient('localhost', 27017)
	cosstores = client['cosstores']
	tab = cosstores[tableName]
	return tab.find()
