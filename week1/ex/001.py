#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: 001.py
@time: 2016/3/26 20:04
"""
import requests
from bs4 import BeautifulSoup
import sys
import os


"""
爬取照片，然后存到相应的文件夹，爬取前20页
"""

mainUrl = 'http://weheartit.com/inspirations/taylorswift?scrolling=true&page=8'
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}



def getImgLink(page):
	"""
	此函数获取图片的下载链接，其中参数page为爬取的页面数量,返回一个包含所有图片下载链接的列表
	"""
	urls = ['http://weheartit.com/inspirations/taylorswift?scrolling=true&page={}'.format(str(i)) for i in range(1,page+1)]
	imgLinks = []
	for url in urls:
		web_data = requests.get(url,headers=header)
		soup = BeautifulSoup(web_data.text,'lxml')
		imageLinks = soup.select('img.entry_thumbnail')
		for imgLink in imageLinks:
			imgLinks.append(imgLink.get('src').replace('superthumb', 'large'))
	return imgLinks

def downImg(downList, folderName):
	for link in downList:
		response = requests.get(link, stream=True)
		totalSize = int(response.headers['Content-Length'])
		if totalSize > 0:
			print('\n[+] Size: %dKB'%(totalSize/1024))
		else:
			print('[+] Size: None')
		try:
			size = 0
			pwd = os.getcwd()
			path_ = pwd + "\\" + folderName + "\\"
			if not os.path.exists(path_):
				os.makedirs('{}'.format(path_))
				with open(path_+link.split('/')[-2]+".jpg", "wb") as img:
					for image in response.iter_content(chunk_size=1024):
						if image:
							img.write(image)
							size += len(image)
							image.flush()
						sys.stdout.write("\rNow: [%d], Total: %d"%(size, totalSize))
						sys.stdout.flush()

			else:
				with open(path_ + link.split('/')[-2] + ".jpg", "wb") as img:
					for image in response.iter_content(chunk_size=1024):
						if image:
							img.write(image)
							size += len(image)
							# image.flush()
						sys.stdout.write("\rNow: [%d], Total: %d" % (size, totalSize))
						sys.stdout.flush()
		except Exception:
			print("Invalid data")


if __name__ == '__main__':
	down = getImgLink(20)
	downImg(down, 'TalorSwift')