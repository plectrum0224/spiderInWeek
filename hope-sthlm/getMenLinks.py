from bs4 import BeautifulSoup
import requests
import pymongo
import time





url = 'http://hope-sthlm.com/man'
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}
def getUrlList(hostUrl, headers):
	webData = requests.get(url, headers=headers)
	soup = BeautifulSoup(webData.text, 'lxml')
	manLinks = soup.select('li.level0.nav-2.active.level-top.parent > ul > li > a')
	urlList = [link.get('href') for link in manLinks]
	return urlList


if __name__ == '__main__':
	# 获取网站男装品类下面的所有主链接，共12个，之后存入数据库中manLinks表中
	client = pymongo.MongoClient('localhost', 27017)
	hopeSthlm = client['hopeSthlm']
	manLinks = hopeSthlm['manLinks']
	for url in getUrlList(url, header):
		data = {
			'link': url
		}
		manLinks.insert_one(data)
