#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: mrporter.py
@time: 2016/3/18 21:40
"""
import os
import re
from bs4 import BeautifulSoup
import requests
import time
import pymongo

hostUrl = 'http://www.mrporter.com'
# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
# 建立数据库
mrporter = client['mrporter']
# 建立表
channelLinksTab = mrporter['channelLinksTab']
subLinks = mrporter['subLinks']



# 获取网站channel,此网站有10个频道，获取每个频道的链接
def getChannelLinks(url):
    header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            }
    web_data = requests.get(url, headers=header)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    channelLinks = soup.select('#menu > ul.parent > li > a')
    for link in channelLinks:
         if link.get('href').split('/')[-1] == 'azdesigners':
             designerLink = link.get('href').split('/')[-1] = '/en-cn/mens/azdesigners/'
             fullLink = hostUrl + designerLink
         elif link.get('href').split('/')[-1] == 'sport':
             sportLink = link.get('href').split('/')[-1] = '/en-cn/mens/sport/'
             fullLink = hostUrl + sportLink
         elif link.get('href').split('/')[-1]  !=  '':
             fullLink = hostUrl + link.get('href') + '/'
         else:
             fullLink = hostUrl + link.get('href')
         channelLinksTab.insert_one({'channelLink': fullLink})
         print("Insert Succeed!!")
    print("Finished!!!")


# 获取频道下面的子链接
def getSubLinks(channel, catas) :
    header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
            }
    web_data = requests.get(channel, headers=header)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if catas == 'azdesigners':
        catas = 'designers'
        picLinks = soup.find_all(href=re.compile('en-cn/mens/{}/'.format(catas)))
        for link in picLinks:
            links = hostUrl + link.get('href')
            print(links)
            subLinks.insert_one({catas: links})
            print('Insert Succeed!!!')
    else:
        picLinks = soup.find_all(href=re.compile('en-cn/mens/{}/'.format(catas)))
        for link in picLinks:
            links = hostUrl + link.get('href')
            print(links)
            subLinks.insert_one({catas: links})
            print('Insert Succeed!!!')
    print('Finished!!')

# 将子链接添加到subLinks表中
# for item in channelLinksTab.find():
#     channelLink = item['channelLink']
#     channelName = channelLink.split('/')[-2].strip()
#     getSubLinks(channelLink, channelName)


# 获取所有图片链接,返回所有链接的列表
def getPicLinks(url):
    linkList = []
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    }
    web_data = requests.get(url, headers=header)
    # time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    picLinks = soup.select('#product-list > div > div > div.designer > a')
    for picLink in picLinks:
        linkList.append( 'http://www.mrporter.com'+picLink.get('href'))
    return linkList

def get_img(link):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    }
    web_data = requests.get(link, headers=header)
    # time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    img = soup.select('#product-page > div > section > section.product-gallery > div.product-image.product-image__cont.js-product-image-cont > img')
    title = soup.select('#product-page > div > section > section.product-details.js-product-details > h1 > span > span')
    for img_, title_ in zip(img, title):
        data = {
            "img": img_.get('alt'),
            "title": title_.get_text()
        }
        return data

def downloadImg(imgUrl, brand, filename):
    response = requests.get(imgUrl, stream=True)
    # time.sleep(1)
    image = response.content
    try:
        pwd = os.getcwd()
        path_ = pwd + "\\" + brand  + '\\'
        if not os.path.exists(path_):
            os.makedirs('{}/{}'.format(os.getcwd(), brand))
            with open(path_  + filename, "wb") as img:
                img.write(image)
                return
        else:
            with open(path_  + filename, "wb") as img:
                img.write(image)
                return
    except Exception:
        print('invalida data')

for item in subLinks.find({'sport':{'$regex':'http://www.mrporter.com/'}}):
    for link in getPicLinks(item['sport']):
        brand = link.split('/')[-3]
        print(link)
        print(brand)
    #     try:
    #         imgLink = 'http:'+get_img(link)['img'].split(' ')[0]
    #         print(get_img(link)['img'])
    #         filename = get_img(link)['title']+'.jpg'
    #         print('downloading......')
    #         downloadImg(imgLink, brand, filename)
    #         print('succeed')
    #     except Exception:
    #         print('invalida data')
    # print('finished one brand... continue')
