#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: ex.py
@time: 2016/3/19 18:09
"""
import pymongo
from bs4 import BeautifulSoup
import requests
import time


#获取每页的所有房源连接，一共获取3页，建立函数,返回一个链接的列表
def getOnePageLinks(pages):
    links = []
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, pages+1)]
    for url in urls:
        web_data = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(web_data.text, 'lxml')
        link = soup.select('#page_list > ul > li > a')
        for item in link:
            links.append(item.get('href'))
    return links

#获取单条链接中房源信息，包括location, price, title
def getHouseInfo(url):
    web_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    location = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
    price = soup.select('#pricePart > div.day_l > span')
    title = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    for location_, price_, title_ in zip(location, price, title):
        data = {
            'location': location_.get_text().strip(),
            'price': int(price_.get_text()),
            'title': title_.get_text()
        }
        return data



#创建数据库，将房屋信息存到数据库中
client = pymongo.MongoClient('localhost', 27017)
houseDB = client['houseDB'] # 建立数据库
infoTab = houseDB['infoTab']# 建立表单

# for link in getOnePageLinks(1):
#     data_ = getHouseInfo(link)
#     print('get one link info...')
#     infoTab.insert_one(data_)
#     print('insert succeed...')
# print('finished')

for item in infoTab.find({'price': {'$lte':300}}):
    print(item)
