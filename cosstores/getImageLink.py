#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: getImageLink.py
@time: 2016/3/24 18:50
"""
import pymongo
import requests
from bs4 import BeautifulSoup

host = 'http://www.cosstores.com'
from cosstores.mongoDB import findLink

header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
	}
def getImageLink(itemType):
	client = pymongo.MongoClient('localhost', 27017)
	cosstores = client['cosstores']
	tab = cosstores['itemLink']
	for i in tab.find({'item': itemType}):
		url = i['link']
		name = i['name']
		item = i['item']
		web_data = requests.get(url,headers=header)
		soup = BeautifulSoup(web_data.text, 'lxml')
		downLinks = soup.select('div.pinch-zoom.hover-zoom')
		for link in downLinks:
			url = link.find_all('img')
			for i in url:
				link = host + i.get('src')
				data = {
					'imgLink': link,
					'name': name,
					'item': item,
				}
				yield (data)


if __name__ == '__main__':
	getImageLink('New')