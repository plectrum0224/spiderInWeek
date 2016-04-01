#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: getDetails.py
@time: 2016/3/29 21:50
"""
import pymongo
import requests
from bs4 import BeautifulSoup
import time

"""
从数据库表中itemLinks取出商品链接，然后抓取商品详细新，此函数需要传入需要爬取得商品频道，将信息存在数据库的details表中
"""

def getDetails(channel):
	"""
	获取指定频道下的所有商品详细信息，之后存入数据库中的details表中
	"""
	client = pymongo.MongoClient('localhost', 27017)
	GanJi = client['Ganji']
	itemLinks = GanJi['itemLinks']
	item =itemLinks.find({"channel" : channel})
	for i in item:
		url = i['link']
		print(url)
		web_data = requests.get(url)
		soup = BeautifulSoup(web_data.text, 'lxml')
		if len(soup.select('h1.title-name')):
			title = soup.select('h1.title-name')[0].get_text()




if __name__ == '__main__':
	getDetails('shouji')