#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: main.py
@time: 2016/3/23 23:38
"""
import pymongo

from cosstores.getImageLink import getImageLink
from cosstores.getItemLinks import getItemLinks
from cosstores.getMenLinks import getMenLinks
from cosstores.mongoDB import saveToDB, findLink


host = 'http://www.cosstores.com'
suburl = 'http://www.cosstores.com/gb/Men'

# saveToDB('menLink', getMenLinks(host, suburl), 'link')
# for link in findLink('menLink'):
# 	print(link['link'])


#将品类链接存放到数据库的itemLink表中
# saveToDB('itemLink', getItemLinks())

#将图片链接存放到数据库的imgLink中
client = pymongo.MongoClient('localhost', 27017)
cosstores = client['cosstores']
tab = cosstores['itemLink']
cata=[]
for i in tab.find():
	cata.append(i['item'])
for t in set(cata):
	saveToDB('imgLinks', getImageLink(t))

