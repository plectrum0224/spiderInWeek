#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: getClothingLinks.py
@time: 2016/3/29 23:16
"""
import os


import requests
import time
import json


def getClothingLinks(page, cataId):
	"""
	从数据库中取出品类的链接，之后获取此链接下所有服装的链接，之后存入
	数据库中的clothing表中，具备两个键值，一个是品类，一个是链接
	"""
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
	}
	urls = ['http://api.net-a-porter.com/MRP/CN/en/90/{}/summaries?categoryIds={}'.format(str(i), str(cataId)) for i in range(0, page*90, 90)]
	for url in urls:
		webData = requests.get(url, headers=header)
		time.sleep(1)
		jsonData = json.loads(webData.text)
		length = len(jsonData['summaries'])
		for i in range(0,length):
			# 这里的imageName得到的是图片的名称
			imageName = jsonData['summaries'][i]['name']
			# 这里的imageLinks是用于组成图片的元素，图片的链接由shots，sizes，url三部分组成的
			imageLinks = jsonData['summaries'][i]['images']
			shots = imageLinks['shots']
			sizes = imageLinks['sizes']
			url = imageLinks['urlTemplate']
			# 这里的shot表示衣服的前后左右视图，sizes代表图片的大小，这里获取所有视图的最大尺寸图片
			try:
				for shot in shots:
					imgUrl = url.replace('{{scheme}}', 'http:').replace('{{shot}}', shot).replace('{{size}}', sizes[0])
					print(imgUrl)
					response = requests.get(imgUrl, stream=True)
					image = response.content
					pwd = os.getcwd()
					path_ = pwd + "\\" + imageName + "\\"
					if not os.path.exists(path_):
						os.makedirs('{}'.format(path_))
						with open(path_ + imgUrl.split('/')[-1], "wb") as img:
							img.write(image)
							print("download succeed")
					else:
						with open(path_ + imgUrl.split('/')[-1], "wb") as img:
							img.write(image)
							print("download succeed")
			except:
				print('invalid')




if __name__ == '__main__':
	getClothingLinks(2, 7050)
