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
@time: 2016/3/20 19:25
"""

from multiprocessing import Pool
from week2.Project58.channelExtract import channelUrlList
from week2.Project58.pageParsing import getLinksFrom
from week2.Project58.pageParsing import getItemInfo
import pymongo

client = pymongo.MongoClient('localhost', 27017)
city58 = client['city58']
urlList = city58['urlList']

def getAllItemFrom(url):
		getItemInfo(url)



def getAllLinksFrom(channel):
	for i in range(1, 101):
		getLinksFrom(channel, i)

if __name__ == '__main__':
	pool = Pool()
	# pool.map(getAllLinksFrom, channelUrlList.split())
	pool.map(getAllItemFrom, 	[item['url'] for item in urlList.find()])

