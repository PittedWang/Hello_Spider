from bs4 import BeautifulSoup
import requests
import time

info = []
url = 'https://movie.douban.com/top250'
urls = ['https://movie.douban.com/top250?start={}&filter='.format(str(i)) for i in range(0,250,25)]
def get_attractions(url,data=None):
    web_data = requests.get(url)
    time.sleep(2) #反爬保护措施
    soup = BeautifulSoup(web_data.text,'lxml')
    titles = soup.select('div > div.info > div.hd > a > span:nth-of-type(1)')
    rates  = soup.select('div > div.info > div.bd > div > span.rating_num')
    counts = soup.select('div > div.info > div.bd > div > span:nth-of-type(4)')
    for title,rate,count in zip(titles,rates,counts):
        data = {
            'Title':title.get_text(),
            'Rate ':rate.get_text(),
            'Count':count.get_text(),
        }
        print(data)
        '''info.append(data)
        for i in info:                                   #筛选Top250中评分大于9的电影(出错了。。。)
             if float(i['rate']) > 9:
                 print(i['title'],i['rate'],i['people'])
                 '''

for single_url in urls:
    get_attractions(single_url)

