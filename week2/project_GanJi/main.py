#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: main.py
@time: 2016/3/27 10:05
"""

from week2.project_GanJi.channelExtract import getChannelList
from week2.project_GanJi.getItemLinks import getItemLinks
from multiprocessing import Pool
import pymongo
"""
获取所有频道下面所有商品链接，之后存入到数据库productDetail
"""

def getProductDetail(channel):
	"""
	获取所有频道下面所有商品链接，之后存入到数据库productDetail
	"""
	for page in range(1, 101):
		getItemLinks(channel, page)

if __name__ == '__main__':
	client = pymongo.MongoClient('localhost', 27017)
	GanJi = client['Ganji']
	channelLinks = GanJi['channelLinks']
	itemLinks = GanJi['itemLinks']
	# channelLink = channelLinks.find()
	# pool = Pool()
	# mainUrl = [link['channel_link'] for link in channelLink]
	# pool.map(getProductDetail, mainUrl)
	item =itemLinks.find({"channel" : "ershoufree"})
	for i in item:
		print(i)








