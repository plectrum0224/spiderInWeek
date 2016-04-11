#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: getMenLinks.py
@time: 2016/3/23 22:28
"""
import re
from bs4 import BeautifulSoup
import requests
import pymongo


host = 'http://www.cosstores.com'
suburl = 'http://www.cosstores.com/gb/Men'

def getMenLinks(hostUrl,  url):
	"""
	获取网站下男装品类下面的所有子链接, 插入到数据库中
	[
	'http://www.cosstores.com/gb/Men/New',
	'http://www.cosstores.com/gb/Men/Essentials',
	'http://www.cosstores.com/gb/Men/Selected',
	'http://www.cosstores.com/gb/Men/Leisure',
	'http://www.cosstores.com/gb/Men/Sale',
	'http://www.cosstores.com/gb/Men/New',
	'http://www.cosstores.com/gb/Men/Coats_Jackets',
	'http://www.cosstores.com/gb/Men/Knitwear',
	'http://www.cosstores.com/gb/Men/Shirts',
	'http://www.cosstores.com/gb/Men/Tops',
	'http://www.cosstores.com/gb/Men/Trousers',
	'http://www.cosstores.com/gb/Men/Denim',
	'http://www.cosstores.com/gb/Men/Tailoring',
	'http://www.cosstores.com/gb/Men/Shorts',
	'http://www.cosstores.com/gb/Men/Leisurewear',
	'http://www.cosstores.com/gb/Men/Underwear',
	'http://www.cosstores.com/gb/Men/Shoes',
	'http://www.cosstores.com/gb/Men/Bags_Wallets',
	'http://www.cosstores.com/gb/Men/Belts',
	'http://www.cosstores.com/gb/Men/Ties',
	'http://www.cosstores.com/gb/Men/Socks'
	]
	"""
	data = {}
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
	}
	web_data = requests.get(url, headers=header)
	soup = BeautifulSoup(web_data.text, 'lxml')
	links = soup.select('#menu > li:nth-of-type(2) > div > div > div.fat-menu-wraper > div')
	for link in links:
		urllist = [hostUrl+url.get('href') for url in link.find_all('a', href=re.compile('/gb/'))][0:21]
		for l in urllist:
			data = {
				"link": l
			}
			client = pymongo.MongoClient('localhost', 27017)
			cosstores = client['cosstores']
			menlink = cosstores['menlink']
			menlink.insert_one(data)


if __name__ == '__main__':
	getMenLinks(host, suburl)

