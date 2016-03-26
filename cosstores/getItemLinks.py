#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: getItemLinks.py
@time: 2016/3/24 17:55
"""
import re
import requests
from bs4 import BeautifulSoup

from cosstores.getLinks import getLinks
from cosstores.mongoDB import findLink


def getItemLinks():
	"""
	此函数获取各个品类的链接，无参数，之后将这些链接存放到以品类命名的表中
	:return: 链接列表
	"""
	# 获取sublink，之后从每个sublink中得到每个品类下面pictures的链接
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
	}
	host = 'http://www.cosstores.com/'
	selector = '#infiload_nav > a'
	for i in findLink('menLink'):
		url = i['link']
		links = getLinks(url,  header, selector)
		for link in links:
			maxpage = int(link.get('data-maxpage'))
			pageId = link.get('href').split('&')[-3]
			urls = [host+"gb/ProductListClientService/loadAdditionalProducts?&{}&page={}&DataType=html".format(pageId, str(page)) for page in range(1, maxpage+1)]
			for url in urls:
				web_data = requests.get(url)
				soup = BeautifulSoup(web_data.text, 'lxml')
				for link in soup.find_all('a'):
					url = link.get('href')
					if url is None:
						pass
					else:
						print(url)
						data = {
							'item': url.split('/')[-3],
							'name':  url.split('/')[-2],
							'link': 'http://www.cosstores.com'+url
						}
						yield (data)



if __name__ == '__main__':
	getItemLinks()
	# for i in getItemLinks():
	# 	print(i['item'])

