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


host = 'http://www.cosstores.com'
suburl = 'http://www.cosstores.com/gb/Men'

def getMenLinks(hostUrl,  url):
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
	}
	web_data = requests.get(url, headers=header)
	soup = BeautifulSoup(web_data.text, 'lxml')
	links = soup.select('#menu > li:nth-of-type(2) > div > div > div.fat-menu-wraper > div')
	for link in links:
		urllist = [hostUrl+url.get('href') for url in link.find_all('a', href=re.compile('/gb/'))][0:21]
		return urllist


if __name__ == '__main__':
	urllists = getMenLinks(host, suburl)
	print(urllists)
