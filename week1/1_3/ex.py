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
@time: 2016/3/17 21:11
"""


'''
抓取标题title，地址address，日租金price，第一张房源图片链接houseImg， 房东图片链接hostImg， 房东性别sex，房东名字name
'''

from bs4 import BeautifulSoup
import requests
import time

# 请求的URL地址
# url = 'http://bj.xiaozhu.com/fangzi/268527300.html'
# 获取网页数据函数
def get_webData(url):
    web_data = requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')

    # 获取对应网页数据
    title = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span.pr5')
    price = soup.select('#pricePart > div.day_l > span')
    houseImg = soup.select('#curBigImage')
    hostImg = soup.select('div.js_box.clearfix > div.member_pic > a > img')
    sex = soup.select('div.js_box.clearfix > div.member_pic > div')
    name = soup.select('div.js_box.clearfix > div.w_240 > h6 > a')

    # 提取具体信息
    for title_,address_,price_,houseImg_,hostImg_,sex_,name_ in zip(title, address, price, houseImg, hostImg, sex, name):
        data = {
            'title': title_.get_text(),
            'address': address_.get_text().strip(),
            'price': price_.get_text(),
            'houseImg': houseImg_.get('src'),
            'hostImg': hostImg_.get('src'),
            'sex': sex_.get('class'),
            'name': name_.get_text(),
        }

        # 判断房东性别
        if data['sex'][0]=='member_ico':
            data['sex'] = 'male'
        else:
            data['sex'] = 'female'

        print(data)


def get_info(page):
    print('Ready....')
    count = 0
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, page+1)]
    for url in urls:
        web_links = requests.get(url)
        time.sleep(2)
        soup = BeautifulSoup(web_links.text, 'lxml')

        links = soup.select('#page_list > ul > li > a')

        for link in links:
            pageLink = (link.get('href'))
            get_webData(pageLink)

        count += 1
        print('page{} finished'.format(count))


get_info(5)
