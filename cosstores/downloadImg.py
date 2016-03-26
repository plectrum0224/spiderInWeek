#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: downloadImg.py
@time: 2016/3/24 23:45
"""
import os

import pymongo
import requests
import sys


def downloadImg(imgUrl, pathName, filename):
	response = requests.get(imgUrl, stream=True)
	total = int(response.headers['Content-Length'])
	print(total)
	if total > 0:
		print('[+] Size: %dKB'%(total/1024))
	else:
		print('[+] Size: None')
	try:
		size = 0
		pwd = os.getcwd()
		path_ = pwd + "\\" + pathName
		if not os.path.exists(path_):
			os.makedirs('{}'.format(path_))
			with open(path_  + filename, "wb") as img:
				for image in response.iter_content(chunk_size=1024):
					if image:
						img.write(image)
						size += len(image)
						img.flush()
					sys.stdout.write("\rNow: [%d], Total: %d"%(size, total))
					sys.stdout.flush()
				return
		else:
			with open(path_  + filename, "wb") as img:
				for image in response.iter_content(chunk_size=1024):
					if image:
						img.write(image)
						size += len(image)
						img.flush()
					sys.stdout.write("\rNow: %s, Total: %d" % (size, total))
					sys.stdout.flush()
				return
	except Exception:
		print('invalida data')

if __name__ == '__main__':
	client = pymongo.MongoClient('localhost', 27017)
	cosstores = client['cosstores']
	tab = cosstores['imgLinks']
	for i in tab.find():
		pathName = i['item'] + '\\' + i['name']  + '\\'
		fileName = i['imgLink'].split('/')[-1]
		url = i['imgLink']
		downloadImg(url, pathName, fileName)