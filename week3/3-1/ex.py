import pymongo

client = pymongo.MongoClient('localhost', 27017)
GJ = client['GJ']
itemLink = GJ['itemLink']
productDetail = GJ['productDetail']

cursor = productDetail.find({}, {'location':1, '_id':1})

for data in cursor:
    if data['location'][1] == '':
        data['location'][1] = '不明'
    productDetail.update({'_id': data['_id']},{'$set':{'location': data['location']}})

areaIndex = []
for dataNew in productDetail.find({}, {'location':1, '_id':0}):
    areaIndex.append(dataNew['location'][1])
area = list(set(areaIndex))
print(area)

areaNum = []
for item in area:
    areaNum.append(areaIndex.count(item))
print(areaNum)

