#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: imitation.py
@time: 2016/3/19 14:20
"""

import pymongo
#创建一个本地客户端连接MongoDB server
client = pymongo.MongoClient('localhost', 27017)
#创建一个名称walden的数据库
walden = client['walden']
#创建一个表单
sheet_tab = walden['sheet_tab']

# #读取本地的txt文本，将文本存到数据库中
# path = 'walden.txt'
# with open(path, 'r') as f:
#     lines = f.readlines()
#     for index, line in enumerate(lines):
#         data = {
#             'index': index,
#             'line': line,
#             'word': len(line.split())
#         }
#         sheet_tab.insert_one(data)

for item in sheet_tab.find({'word':{'$lt':5}}):
    print(item)
