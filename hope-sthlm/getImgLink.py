import requests
import time
from bs4 import BeautifulSoup
import pymongo
header = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
}


client = pymongo.MongoClient('localhost', 27017)
hopeSthlm = client['hopeSthlm']
itemLink = hopeSthlm['itemLink']
imgLink = hopeSthlm['imgLink']
for url in list(itemLink.find()):
	try:
		webData = requests.get(url['link'], headers=header)
		# time.sleep(2)
		soup = BeautifulSoup(webData.text, 'lxml')
		imgUrls = soup.select('div.swipe__wrapper > a')
		for img in [url.get('href') for url in imgUrls]:
			print(img)
			imgName = img.split('/')[-1]
			data = {
				'imgName': imgName,
				'imgLink': img
			}
			imgLink.insert_one(data)
			print("插入成功")
	except:
		print('Error')


