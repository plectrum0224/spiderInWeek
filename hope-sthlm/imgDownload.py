import os

import pymongo
import requests
import sys


def downloadImg(imgUrl, pathName, filename):
	try:
		response = requests.get(imgUrl, stream=True)
		total = int(response.headers['Content-Length'])
		if total > 0:
			print('[+] Size: %dKB '%(total/1024))
		else:
			print('[+] Size: None')

		size = 0
		pwd = os.getcwd()
		path_ = pwd + "\\" + pathName
		if not os.path.exists(path_):
			os.makedirs('{}'.format(path_))
			with open(path_  + filename, "wb") as img:
				for image in response.iter_content(chunk_size=1024):
					if image:
						img.write(image)
						size += len(image)
						img.flush()
					sys.stdout.write("\rNow: [%d], Total: %d "%(size, total))
					sys.stdout.flush()
				return
		else:
			with open(path_  + filename, "wb") as img:
				for image in response.iter_content(chunk_size=1024):
					if image:
						img.write(image)
						size += len(image)
						img.flush()
					sys.stdout.write("\rNow: %s, Total: %d" % (size, total))
					sys.stdout.flush()
				return
	except Exception:
		print('invalida data')

if __name__ == '__main__':
	client = pymongo.MongoClient('localhost', 27017)
	hopeSthlm = client['hopeSthlm']
	itemLink = hopeSthlm['itemLink']
	imgLink = hopeSthlm['imgLink']
	print(imgLink.find().count())
	count = 0
	for i in imgLink.find():
		print(i)
		pathName = 'pics'  + '\\'
		fileName = str(count) + i['imgName']
		url = i['imgLink']
		print(url)
		downloadImg(url, pathName, fileName)
		count += 1
		print('<-----------------------{}------------------------>'.format(count))
