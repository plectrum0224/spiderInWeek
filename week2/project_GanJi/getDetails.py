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
import re
import requests
from bs4 import BeautifulSoup
import time


def getDetails():
	client = pymongo.MongoClient('localhost', 27017)
	GJ = client['GJ']
	itemLink = GJ['itemLink']
	productDetail = GJ['productDetail']
	for data in itemLink.find({'crawled': False}):
		if "bj.ganji.com" in data['itemUrl']:
			web_data = requests.get(data['itemUrl'])
			soup = BeautifulSoup(web_data.text, 'lxml')
			if web_data.status_code == 404 or soup.find_all('p', class_='error-tips1'):
				print("product info have been deleted")
			else:
				_id = data['itemUrl'].split('/')[-1].split('x.')[0]
				detailData = {
					'id': _id,
					'url': data['itemUrl'],
					'title': soup.select('h1.title-name')[0].get_text(),
					'postTime': soup.select('i.pr-5')[0].get_text().strip().split(' ')[0],
					'price': soup.select('i.f22.fc-orange.f-type')[0].get_text(),
					'cata': list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings),
					'location': list(map(lambda x: x.text, soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
					'quality': list(map(lambda x: list(x.stripped_strings)[1], list(filter(lambda x: x.find_all(text=re.compile("新旧程度：")), soup.select('ul.second-det-infor.clearfix > li'))))),
				}
				print('process: ', data)
				itemLink.update({'_id': data['_id']}, {'$set': {'crawled': True}})
				productDetail.insert_one(detailData)
				time.sleep(2)

if __name__ == '__main__':
	getDetails()