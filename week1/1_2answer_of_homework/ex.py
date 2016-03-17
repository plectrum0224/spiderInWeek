#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://
@software: PyCharm
@file: ex.py
@time: 2016/3/16 20:23
"""
import re

from bs4 import BeautifulSoup

with open('1_2answer_of_homework/1_2_homework_required/index.html', 'r') as webData:

    soup = BeautifulSoup(webData, 'lxml')

    images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    reviews = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')


    # print(images, prices, titles, reviews, stars, sep='\n#-------------------------------#\n')



print(list(zip(images, prices, titles, reviews, stars)))

# for image, price, title, review, star in zip(images, prices, titles, reviews, stars):
#     data = {
#         'title': title.get_text(),
#         'price': price.get_text(),
#         'review': review.get_text(),
#         'image': image.get('src'),
#         'star': len(star.find_all("span", class_='glyphicon glyphicon-star'))
#     }
#     print(data)



# {'price': '$24.99', 'title': 'EarPod', 'review': '65 reviews', 'image': 'img/pic_0000_073a9256d9624c92a05dc680fc28865f.jpg'}
# {'price': '$64.99', 'title': 'New Pocket', 'review': '12 reviews', 'image': 'img/pic_0005_828148335519990171_c234285520ff.jpg'}
# {'price': '$74.99', 'title': 'New sunglasses', 'review': '31 reviews', 'image': 'img/pic_0006_949802399717918904_339a16e02268.jpg'}
# {'price': '$84.99', 'title': 'Art Cup', 'review': '6 reviews', 'image': 'img/pic_0008_975641865984412951_ade7a767cfc8.jpg'}
# {'price': '$94.99', 'title': 'iphone gamepad', 'review': '18 reviews', 'image': 'img/pic_0001_160243060888837960_1c3bcd26f5fe.jpg'}
# {'price': '$214.5', 'title': 'Best Bed', 'review': '18 reviews', 'image': 'img/pic_0002_556261037783915561_bf22b24b9e4e.jpg'}
# {'price': '$500', 'title': 'iWatch', 'review': '35 reviews', 'image': 'img/pic_0011_1032030741401174813_4e43d182fce7.jpg'}
# {'price': '$15.5', 'title': 'Park tickets', 'review': '8 reviews', 'image': 'img/pic_0010_1027323963916688311_09cc2d7648d9.jpg'}
