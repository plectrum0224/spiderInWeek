#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: Dave
@license: No Licence 
@contact: plectrum@outlook.com
@site: http://
@software: PyCharm
@file: channelExtract.py
@time: 2016/3/27 9:29
"""

import requests
from bs4 import BeautifulSoup
import pymongo
import time

# build the database for Ganji project, the database
# name is Ganji, have a table named channelinks save the channel links
client = pymongo.MongoClient('localhost', 27017)
GJ = client['GJ']
channelLinks = GJ['channelLink']

# define the function get the channel links, have one parameter get the host url
def getChannelList(hostUrl):
	web_data = requests.get(hostUrl)
	time.sleep(2)
	soup = BeautifulSoup(web_data.text, 'lxml')
	clinks = soup.select('dl.fenlei > dt > a')
	linkList= [hostUrl.replace('/wu', i.get('href'))  for i in clinks]
	for link in linkList:
		# if the link existed break the current loop and get a next link
		if channelLinks.find_one({'channelLink': link}):
			continue
		# insert 2 segments for the table, channelLink is the href link and
		# crawled indicate the link get content or not
		channelLinks.insert_one({'channelLink': link, 'crawled': False})
		print('<<------{}------Insert Succeed------>>'.format(link))
		time.sleep(2)
	print('Insert Done')


if __name__ == '__main__':
	url = 'http://bj.ganji.com/wu'
	getChannelList(url)
