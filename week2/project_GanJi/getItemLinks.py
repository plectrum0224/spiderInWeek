#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: getItemLinks.py
@time: 2016/3/27 9:29
"""
import re

import pymongo
import requests
from bs4 import BeautifulSoup
import time


def getItemLinks(channel, page, whoSeal = None):
	"""
	从数据库中获取频道链接，之后爬取个频道连接下的商品链接
	传入三个参数
	channel 频道链接
	page 爬取页数
	whoSeal 默认参数为个人，如选择商家，则将此参数设为'a2'
	返回链接存入数据中itemLinks表中
	"""
	client = pymongo.MongoClient('localhost', 27017)
	GanJi = client['Ganji']
	itemLinks = GanJi['itemLinks']
	if whoSeal is None:
		url = '{}o{}'.format(channel, str(page))
	else:
		url = '{}{}o{}'.format(channel, whoSeal, page)
	web_data = requests.get(url)
	time.sleep(5)
	print(url)
	soup = BeautifulSoup(web_data.text, 'lxml')
	# 获取商品链接, 网页中没有pageBox标签则表示到最后一页
	if soup.find('div', 'pageBox'):
		links = soup.find_all('a', class_=re.compile('ft-tit|com-title'))
	# 插入商品链接到数据库
		for link in links:
			print(link.get('href'))
			itemLinks.insert_one({'channel': channel.split('/')[-2], 'link': link.get('href')})
			print('<<------Insert Succeed....next....------>>')
			print(link.get('href'))
		print('Insert Done')
	else:
		pass

if __name__ == '__main__':
	getItemLinks("http://bj.ganji.com/ershoufree/", 55)