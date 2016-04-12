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
from multiprocessing import Pool
client = pymongo.MongoClient('localhost', 27017)
GJ = client['GJ']
channelLinks = GJ['channelLink']
pageLink = GJ['pageLink']
itemLink = GJ['itemLink']

def getItemLinks(channel, page, whoSeal='o'):
	pageUrl = '{}{}{}/'.format(channel, whoSeal, str(page))
	# if find the page link in the table 'pageLink', end the function
	if pageLink.find_one({'pageUrl': pageUrl}):
		return
	# get the page content from the page link
	web_data = requests.get(pageUrl)
	soup = BeautifulSoup(web_data.text, 'lxml')
	# if not find the pageBox, means all the sub page finished, end the function
	if soup.find('div', 'pageBox'):
		for link in soup.find_all('a', class_=re.compile('ft-tit|com-title')):
			itemUrl = link.get('href')
			# if find the item link in the table 'itemLink', end the current loop, the handle the next link
			if itemLink.find_one({'itemUrl': itemUrl}):
				continue
			itemLink.insert({'itemUrl': itemUrl, 'crawled': False})
			print(itemUrl)
		pageLink.insert({'pageUrl': pageUrl})
		print(pageUrl)
		time.sleep(2)

def getAllLinks(channel):
	for i in range(1,101):
		getItemLinks(channel, i)

if __name__ == '__main__':
	pool = Pool()
	pool.map(getAllLinks, [link['channelLink'] for link in channelLinks.find()])
	# for i in range(1,101):
	# 	getItemLinks('http://bj.ganji.com/qitawupin/', i)
