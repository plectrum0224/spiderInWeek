#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: channelExtract.py
@time: 2016/3/27 9:29
"""

import requests
from bs4 import BeautifulSoup
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
GanJi = client['Ganji']
channelLinks = GanJi['channelLinks']


def getChannelList(hostUrl):
	"""
	获取网站下面各频道主链接，通过此主链接获取商品条目链接
	将主链接存入数据库
	:return 链接列表
	"""
	web_data = requests.get(hostUrl)
	time.sleep(2)
	soup = BeautifulSoup(web_data.text, 'lxml')
	clinks = soup.select('dl.fenlei > dt > a')
	linkList= [hostUrl.replace('/wu', i.get('href'))  for i in clinks]
	# 插入频道链接到数据库GanJi下面的channelLinks表中
	for link in linkList:
		channelLinks.insert_one({'channel_link': link})
		print('<<------Insert Succeed....next....------>>')
	print('Insert Done')






if __name__ == '__main__':
	url = 'http://bj.ganji.com/wu'
	getChannelList(url)
	"""
	['http://bj.ganji.com/jiaju/', 'http://bj.ganji.com/rirongbaihuo/', 'http://bj.ganji.com/shouji/', 'http://bj.ganji.com/shoujihaoma/', 'http://bj.ganji.com/bangong/', 'http://bj.ganji.com/nongyongpin/', 'http://bj.ganji.com/jiadian/', 'http://bj.ganji.com/ershoubijibendiannao/', 'http://bj.ganji.com/ruanjiantushu/', 'http://bj.ganji.com/yingyouyunfu/', 'http://bj.ganji.com/diannao/', 'http://bj.ganji.com/xianzhilipin/', 'http://bj.ganji.com/fushixiaobaxuemao/', 'http://bj.ganji.com/meironghuazhuang/', 'http://bj.ganji.com/shuma/', 'http://bj.ganji.com/laonianyongpin/', 'http://bj.ganji.com/xuniwupin/', 'http://bj.ganji.com/qitawupin/', 'http://bj.ganji.com/ershoufree/', 'http://bj.ganji.com/wupinjiaohuan/']
	"""