# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:59:13 2021

@author: MLZ107
"""

import requests
import string
from bs4 import BeautifulSoup
from urllib import parse

url='http://m.bendibao.com/city.php'
page= requests.get(url = url)
page.encoding='GBK2312'

#print(page.text)
fp = open('bendibao.txt','w',encoding='utf-8')
fp.write(page.text)
fp.close()

soup=BeautifulSoup(page.text,'html.parser')
soup=soup.find_all('a')
city_sum_list={}
for i in soup:
    if i.has_attr('href'):
        if i.string in string.ascii_uppercase or i.string in ['移动版','电脑版','意见建议']:
            continue
        city_sum_list[i.string] = i['href']
#print(city_sum_list)
#保存到TXT文件
fp = open('本地宝城市网址.txt','w',encoding='utf-8')
for i in city_sum_list:
    fp.write(i)
    fp.write('\t')
    fp.write(city_sum_list[i])
    fp.write('\n')
fp.close()

city_name_list = ["北京","上海","广州","成都","杭州","重庆","西安","苏州",
                  "武汉","南京","天津","郑州","长沙","东莞","佛山","青岛","沈阳"]       
dest_url_list = []
for i in city_name_list:
    dest_url_list.append(city_sum_list[i])
#print(dest_url_list)
#保存到TXT文件
fp = open('本地宝一线城市网址.txt','w',encoding='utf-8')
for i in city_name_list:
    fp.write(i)
    fp.write('\t')
    fp.write(city_sum_list[i])
    fp.write('\n')
fp.close()


query_url_list=[]
n=0
for i in dest_url_list:
    page = requests.get(url=i)
    page.encoding = 'GBK2312'
    soup = BeautifulSoup(page.text,"html.parser")
    soup = soup.select(".search")
    #print(type(soup))
    query = soup[0]['href']
    #print(type(query)) #<class 'str'>
    #print(query.split('?')[0]) 
    key_str = parse.quote(city_name_list[n] + "2021人才落户及补贴政策")
    query_url = query.split('?')[0]+'?q='+key_str+'&click=1&'+query.split('?')[1]+'&nsid='
    query_url_list.append(query_url)
    #print(query_url)
    n += 1
#报存到TXT文件
n = 0
fp = open('./一线城市人才引进网址.txt','w',encoding='utf-8')
for i in query_url_list:
    fp.write(city_name_list[n]+'\t')
    fp.write(i+'\n')
    n += 1
fp.close()

page_num = 2
query_url_city_list=[]
for i in query_url_list:
    page = requests.get(url = i)
    page.encoding = 'GBK2312'
    soup = BeautifulSoup(page.text,'html.parser')
    #print(soup)
    soup = soup.select('div > h3 > a',limit = page_num)
    query_url_city_list.append(soup[0]['href'])
    query_url_city_list.append(soup[1]['href'])
#print(query_url_city_list)
fp = open('人才引进具体内容网址.txt','w',encoding='utf-8')
for i in query_url_city_list:
    fp.write(i+'\n')
fp.close()  

# i = 0 
# while(i < len(city_name_list)):
#     if(city_name_list[i] == '武汉'):
#         break
#     i += 1
# #print(i)
# url = query_url_city_list[2*i]
# page = requests.get(url = url)
# page.encoding = 'GBK2312'
# soup = BeautifulSoup(page.text,'html.parser')
