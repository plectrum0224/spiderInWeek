#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: subZone.py
@time: 2016/3/20 20:29
"""
import os
import re
from bs4 import BeautifulSoup
import requests

# urls = ['http://jandan.net/ooxx/page-{}'.format(str(i)) for i  in range(1500,1900)]
# header = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
#     'Cookies': '_gat=1; 2566364397=572; _ga=GA1.2.1097038812.1458481950; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1457230812,1458481950; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1458483784'
#         }
# def downloadImg(imgUrl, filename):
#     response = requests.get(imgUrl, stream=True)
#     # time.sleep(1)
#     image = response.content
#     try:
#         pwd = os.getcwd()
#         path_ = pwd + "\\" + 'pic'  + '\\'
#         if not os.path.exists(path_):
#             os.makedirs('{}/{}'.format(os.getcwd(), 'pic'))
#             with open(path_  + filename, "wb") as img:
#                 img.write(image)
#                 return
#         else:
#             with open(path_  + filename, "wb") as img:
#                 img.write(image)
#                 return
#     except Exception:
#         print('invalida data')
#
#
# for url in urls:
#     web_data = requests.get(url, headers=header)
#     soup = BeautifulSoup(web_data.text, 'lxml')
#
#     imglinks = soup.find_all('img')
#     for img in imglinks:
#         filename = img.get('src').split('/')[-1]
#         print(filename)
#         downloadImg(img.get('src'), filename)


def getXSRF(r):
	cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
	strlist = cer.findall(r.text)
	return strlist[0]



s = requests.session()
r = s.get('http://www.zhihu.com/')
print (r.cookies)
print(r.cookies['_xsrf'])























