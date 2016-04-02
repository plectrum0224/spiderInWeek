#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: 002.py
@time: 2016/3/26 21:54
"""

"""
下载58网站的商品链接，包括商品类目，标题，发帖时间，价格，成色，区域，浏览量
url = 'http://bj.58.com/pbdn/0/pn{page}/'
"""

import requests
from bs4 import BeautifulSoup
import time



# 获取商品链接的函数，通过page参数指定抓取多少页面
def productLinks(page):
	"""
	productLinks函数传入一个page参数，爬取页面数量，返回商品链接的列表productLink[]
	"""
	urls = ['http://bj.58.com/pbdn/0/pn{}/'.format(str(i)) for i in range(1, page+1)]
	for url in urls:
		web_data = requests.get(url)
		time.sleep(1)
		soup = BeautifulSoup(web_data.text,'lxml')
		links = soup.select('td.t > a.t')
		for productLink in links:
			if 'bj.58.com' in productLink.get('href'):   # 只收集58的链接，转转及推广商品的链接不要
				yield productLink.get('href')



# 获取商品详情的函数
def getProductDetail(page):
	"""
	返回产品详情的字典结构
	{
 ‘item’:
	'title':
	'postTime':
	'price':
	'quality':
	'zone':
	'pv':
	}
	"""
	data = {}
	for url in productLinks(page):     # 从列表中取出链接
		print(url)
		web_data = requests.get(url)
		time.sleep(1)
		soup = BeautifulSoup(web_data.text,'lxml')
		# 取类目
		for item in soup.select('span:nth-of-type(3) > a'):
			data['item'] = item.get_text()
		# 取标题
		for title in soup.select('div.col_sub.mainTitle > h1'):
			data['title'] = title.get_text()
		# 取发布时间
		for postTime in soup.select('ul.mtit_con_left.fl > li.time'):
			data['postTime'] = postTime.get_text()
		# 取价格
		for price in soup.select('span.price.c_f50'):
			data['price'] = price.get_text()
		# 取成色，如果没有显示None
		if len(soup.select('li:nth-of-type(2) > div.su_con > span')):
			for quality in soup.select('li:nth-of-type(2) > div.su_con > span'):
				data['quality'] = quality.get_text()
		else:
			data['quality'] = 'None'
		# 取区域，如果没有显示None
		if len(soup.select('span.c_25d')):
			for zone in soup.select('span.c_25d'):
				data['zone'] = list(zone.stripped_strings)
		else:
			data['zone'] = 'None'

		header = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
		}
		productID = url.split('=')[-1][:-2]
		# 从这个链接取出访问量
		viewUrl = 'http://jst1.58.com/counter?infoid={}'.format(productID)
		pvData = requests.get(viewUrl,headers=header)
		pv = pvData.text.split('=')[-1]
		data['pv'] = pv
		print(data)



if __name__ == '__main__':
	getProductDetail(1)



