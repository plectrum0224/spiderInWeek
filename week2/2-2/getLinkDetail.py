#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: getLinkDetail.py
@time: 2016/3/20 10:15
"""
import re

import time
from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['linksInfo']
table = db['phoneLinks']
phoneInfo = db['phoneInfo']

def getLinkDetail():
    for link in table.find({'link': {'$regex':'http://bj.58.com'}}):
        linkInfo = link['link']
        web_data = requests.get(linkInfo)
        time.sleep(1)
        soup = BeautifulSoup(web_data.text, 'lxml')
        title = soup.title.text
        price = soup.select('span.price.c_f50')[0].text.strip()
        contactor = soup.select('span.f20.arial.c_f50')[0].text.strip()
        phoneInfo.insert_one({'title':title, 'price':price, 'contactor':contactor})
        print("insert succeed...")


getLinkDetail()