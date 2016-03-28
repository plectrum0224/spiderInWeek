#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: channelExtract.py
@time: 2016/3/20 17:38
"""
from bs4 import BeautifulSoup
import requests
import time
import pymongo




# 函数： 获取所有频道的链接

start_url = 'http://bj.58.com/sale.shtml'
hostUrl = 'http://bj.58.com'
def getChannelUrl(url):
	web_data = requests.get(url)
	soup = BeautifulSoup(web_data.text, 'lxml')
	links = soup.select('ul.ym-submnu > li > b > a')
	for link in links:
		channelUrl = hostUrl + link.get('href')
		print(channelUrl)

# getChannelUrl(start_url)

channelUrlList = '''
	http://bj.58.com/shouji/
	http://bj.58.com/tongxunyw/
	http://bj.58.com/danche/
	http://bj.58.com/fzixingche/
	http://bj.58.com/diandongche/
	http://bj.58.com/sanlunche/
	http://bj.58.com/peijianzhuangbei/
	http://bj.58.com/diannao/
	http://bj.58.com/bijiben/
	http://bj.58.com/pbdn/
	http://bj.58.com/diannaopeijian/
	http://bj.58.com/zhoubianshebei/
	http://bj.58.com/shuma/
	http://bj.58.com/shumaxiangji/
	http://bj.58.com/mpsanmpsi/
	http://bj.58.com/youxiji/
	http://bj.58.com/jiadian/
	http://bj.58.com/dianshiji/
	http://bj.58.com/ershoukongtiao/
	http://bj.58.com/xiyiji/
	http://bj.58.com/bingxiang/
	http://bj.58.com/binggui/
	http://bj.58.com/chuang/
	http://bj.58.com/ershoujiaju/
	http://bj.58.com/bangongshebei/
	http://bj.58.com/diannaohaocai/
	http://bj.58.com/bangongjiaju/
	http://bj.58.com/ershoushebei/
	http://bj.58.com/yingyou/
	http://bj.58.com/yingeryongpin/
	http://bj.58.com/muyingweiyang/
	http://bj.58.com/muyingtongchuang/
	http://bj.58.com/yunfuyongpin/
	http://bj.58.com/fushi/
	http://bj.58.com/nanzhuang/
	http://bj.58.com/fsxiemao/
	http://bj.58.com/xiangbao/
	http://bj.58.com/meirong/
	http://bj.58.com/yishu/
	http://bj.58.com/shufahuihua/
	http://bj.58.com/zhubaoshipin/
	http://bj.58.com/yuqi/
	http://bj.58.com/tushu/
	http://bj.58.com/tushubook/
	http://bj.58.com/wenti/
	http://bj.58.com/yundongfushi/
	http://bj.58.com/jianshenqixie/
	http://bj.58.com/huju/
	http://bj.58.com/qiulei/
	http://bj.58.com/yueqi/
	http://bj.58.com/tiaozao/
'''