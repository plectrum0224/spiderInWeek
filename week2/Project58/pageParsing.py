#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: pageParsing.py
@time: 2016/3/20 17:57
"""

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
city58 = client['city58']
urlList = city58['urlList']
itemList = city58['itemList']

# spider1 抓取所有商品链接
def getLinksFrom(channel, pages, whoSells=0):
	# 'http://bj.58.com/shouji/0/pn2/'
	listView = '{}{}/pn{}/'.format(channel, str(whoSells), str(pages))
	web_data = requests.get(listView)
	soup = BeautifulSoup(web_data.text, 'lxml')
	if soup.find('td', 't'):
		for link in soup.select('td.t a.t'):
			item_link = link.get('href').split('?')[0]
			urlList.insert_one({'url': item_link})
			print(item_link)
	else:
		pass

def getItemInfo(url):
	wb_data = requests.get(url)

	soup = BeautifulSoup(wb_data.text, 'lxml')
	try:
		noExist = '404' in soup.find('script', type='text/javascript').get('src').split('/')
		if noExist:
			pass
		else:
			title = soup.title.text
			price = soup.select('span.price.c_f50')[0].text
			date = soup.select('.time')[0].text
			area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find_all('span', 'c_25d') else None
			itemList.insert_one({'title': title, 'price': price, 'date': date, 'area': area})
			print({'title': title, 'price': price, 'date': date, 'area': area})
	except Exception:
		print('invalid data')







# getLinksFrom('http://bj.58.com/shouji/', 2)


