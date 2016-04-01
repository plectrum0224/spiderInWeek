#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: getCataLinks.py
@time: 2016/3/29 22:59
"""


import requests
from bs4 import BeautifulSoup
import time
import pymongo
client = pymongo.MongoClient('localhost', 27017)
mrporter = client['mrporter']
cataLinks = mrporter['cataLinks']


def getCataLinks(channel):
	"""
	获取指定品类下的所有子链接，之后存入数据库mrporter下的cataLinks表中
	指定品类参数
	"""
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
	}
	cataUrl = 'http://www.mrporter.com/en-cn/mens/' + channel
	webData = requests.get(cataUrl, headers=header)
	soup = BeautifulSoup(webData.text, 'lxml')
	links = soup.select('a.pl-categories__link')
	for link in links:
		url = link.get('href')
		if len(url.split('/'))==5:
			subLink = 'http://www.mrporter.com' + url
			cataLinks.insert_one({'cataLink': subLink})
			print('Insert Succeed')
	print('Insert Done')

if __name__ == '__main__':
	getCataLinks('clothing')