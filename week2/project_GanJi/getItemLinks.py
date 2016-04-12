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
client = pymongo.MongoClient('localhost', 27017)
GJ = client['GJ']
pageLink = GJ['pageLink']
itemLink = GJ['itemLink']

def getItemLinks(channel, page, whoSeal='o'):
	url = '{}{}{}/'.format(channel, whoSeal, str(page))
	if pageLink.find_one({'pageUrl': url}):
		return
	web_data = requests.get(url)
	soup = BeautifulSoup(web_data.text, 'lxml')
	if soup.find('div', 'pageBox'):
		for link in soup.select('.js-item > a'):
			itemUrl = link.get('href')
			if itemLink.find_one({'itemUrl': itemUrl}):
				continue
			itemLink.insert({'itemUrl': itemUrl, 'crawled': False})
			print(itemUrl)
		pageLink.insert({'pageUrl': url})
		print(url)
		time.sleep(2)

if __name__ == '__main__':
	for i in range(1,10):
		getItemLinks("http://bj.ganji.com/jiaju/", i)