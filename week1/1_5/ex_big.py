from bs4 import BeautifulSoup
import requests
import time

# 获取页面链接
def getLinks(page):
    urls = ['http://bj.58.com/pbdn/0/pn{}/?PGTID=0d305a36-0000-1a75-c46e-ec599a8a114a&ClickID=2'.format(str(i)) for i in range(0, page+1)]
    links58 = []
    for url in urls:
        web_data = requests.get(url)
        time.sleep(2)
        soup = BeautifulSoup(web_data.text, 'lxml')
        productLinks = soup.select('td.t > a')
        for productLink in productLinks:
            if productLink.get('href')[0:16] == 'http://bj.58.com':
                links58.append(productLink.get('href'))
    return links58

# 获取链接详情
def getInfo(link):
    web_data = requests.get(link)
    time.sleep(2)
    soup = BeautifulSoup(web_data.text, 'lxml')

    item = soup.select('#header > div.breadCrumb.f12 > span:nth-of-type(3) > a')
    title = soup.select('#content > div.person_add_top.no_ident_top > div.per_ad_left > div.col_sub.mainTitle > h1')
    postTime = soup.select('#index_show > ul.mtit_con_left.fl > li.time')
    price = soup.select('div.col_sub.sumary > ul > li:nth-of-type(1) > div.su_con > span')
    quality = soup.select('div.col_sub.sumary > ul > li:nth-of-type(2) > div.su_con > span')
    zone = soup.select('div.col_sub.sumary > ul > li:nth-of-type(3) > div.su_con > span')
    pv =

    for item_, title_, postTime_, price_, quality_, zone_ in zip(item, title, postTime, price, quality, zone):
        data = {
            "item": item_.get_text(),
            "title":title_.get_text(),
            "postTime": postTime_.get_text(),
            "price": price_.get_text(),
            "quality":quality_.get_text().strip(),
            "zone":zone_.get_text().strip().replace('\t', '').replace('\n', '')
        }

        print(data)
if __name__ == '__main__':
    for link in getLinks(2):
        getInfo(link)