from bs4 import BeautifulSoup
import requests

url = 'https://knewone.com/things/categories/sheng-huo?page=1'
def getImgs(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('a.cover-inner > img')
    print(imgs)
    for img in imgs:
        imgLink = img.get('src')
        imgDesc = img.get('alt').strip()
        filename = imgDesc + '.jpg'
        downloadImg(imgLink, filename)

def getPages(start, end):
    for item in range(start, end):
        urls = url + str(item)
        getImgs(urls)

def downloadImg(imgUrl, filename):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    try:
        with open("C:\\Users\Dave\\PycharmProjects\\spiderInWeek\\week1\\1_4\\imgs\\" +filename, "wb") as img:
            img.write(image)
            return
    except Exception:
        print('invalida data')



if __name__ == '__main__':
    getPages(1,1000)