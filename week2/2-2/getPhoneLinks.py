#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: getPhoneLinks.py
@time: 2016/3/20 9:41
"""

from bs4 import BeautifulSoup
import requests
import pymongo
import time

# 数据库名称：linksInfo
# 表名称：phoneLinks 存放所有电话号码链接
client = pymongo.MongoClient('localhost', 27017)
linksInfo = client['linksInfo']
phoneLinks = linksInfo['phoneLinks']
# http://bj.58.com/shoujihao/0/pn3/
# 获取手机的标题和链接，然后将标题和链接全部存到数据库中
# 函数具备一个页码参数，即总共抓取多少页，pnx，其中x代表页码
# 函数具备一个抓取个人还是商家的参数，个人=0， 商家=1
hostUrl = 'http://bj.58.com/shoujihao/'
def getPhoneLinks(pages, whoSales=1):
    urls = ['{}{}/pn{}/'.format(hostUrl, str(whoSales), str(i)) for i in range(1, pages+1)]
    for url in urls:
        web_data = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(web_data.text, 'lxml')
        links = soup.select('#infolist > div > ul > div.boxlist > ul > li > a.t')
        phones = soup.select('#infolist > div > ul > div.boxlist > ul > li > a.t > strong')
        for link, phone in zip(links, phones):
            data = {
                'link': link.get('href'),
                'title': phone.get_text()
            }
            phoneLinks.insert_one(data)
            print("insert succeed...")


getPhoneLinks(50)