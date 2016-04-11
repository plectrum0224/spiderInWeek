import pymongo
import requests
from bs4 import BeautifulSoup
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}
client = pymongo.MongoClient('localhost', 27017)
hopeSthlm = client['hopeSthlm']
manLinks = hopeSthlm['manLinks']
for link in (list(manLinks.find())):
	webData = requests.get(link['link'], headers=header)
	soup = BeautifulSoup(webData.text, 'lxml')
	itemLinks = soup.select('div.product__media > a')
	urlList = [link.get('href') for link in itemLinks]
	itemLink = hopeSthlm['itemLink']
	for url in urlList:
		itemName = url.split('/')[-1]
		data = {
			'itemName': itemName,
			'link': url,
		}
		itemLink.insert_one(data)


