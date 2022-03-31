# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:11:04 2021

@author: MLZ107
"""

from bs4 import BeautifulSoup
import requests

# page = requests.get(url = 'http://zhannei.baidu.com/cse/search?q=2021%E6%AD%A6%E6%B1%89%E4%BA%BA%E6%89%8D%E5%BC%95%E8%BF%9B&click=1&s=5547445145785787491&nsid=')
# page.encoding = 'GBK2312'
# soup = BeautifulSoup(page.text,'html.parser')
# #print(soup.select('div > h3 > a'))
# result = soup.select('div > h3 > a',limit=2)

#print(result)

# query0 = result[0]['href']
# query1 = result[1]['href']
# print(query0,query1)
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

page = requests.get(url = 'http://wh.bendibao.com/live/202078/113158.shtm')
page.encoding = 'GBK2312'
soup = BeautifulSoup(page.text,'html.parser')

fp = open('./武汉人才引进政策.txt','a',encoding='utf-8')
result = soup.find_all(attrs={'class':'title daoyu'})
result = soup.select('div > h1 > strong')
#print(result[0].text)
fp.writelines(result[0].text+'\n')
result = soup.find_all(class_='time')
#print(result[0].text)
fp.writelines(result[0].text+'\n')

result = soup.select('.content')
soup = BeautifulSoup(str(result[0]),'html.parser')

i = soup.find('p')
#print(i.text)
fp.writelines(i.text+'\n')
for i in soup.p.next_siblings:
    if i.name == 'div':
        break
    #print(i.text)
    fp.writelines(i.text+'\n')
    s = i.find('a')
    if s != None:
        #print(str(s['href'])) 
        fp.writelines(s['href']+'\n')
fp.close()

page = requests.get(url = 'http://wh.bendibao.com/live/2014425/54873.shtm')
page.encoding = 'GBK2312'
soup = BeautifulSoup(page.text,'html.parser')

fp = open('./武汉人才引进政策.txt','a',encoding='utf-8')
result = soup.find_all(attrs={'class':'title daoyu'})
result = soup.select('div > h1 > strong')
#print(result[0].text)
fp.writelines(result[0].text+'\n')
result = soup.find_all(class_='time')
#print(result[0].text)
fp.writelines(result[0].text+'\n')

result = soup.select('.content')
soup = BeautifulSoup(str(result[0]),'html.parser')

i = soup.find('p')
#print(i.text)
fp.writelines(i.text+'\n')
for i in soup.p.next_siblings:
    if i.name == 'div':
        break
    #print(i.text)
    fp.writelines(i.text+'\n')
    s = i.find('a')
    if s != None:
        #print(str(s['href'])) 
        fp.writelines(s['href']+'\n')
fp.close()

#print(soup)
# result = soup.div.stripped_strings
# print(list(result))


#element = soup.p.string
#print(element) 

#print(type(soup))   #<class 'bs4.BeautifulSoup'>
#print(soup.select('.leading'))

#result = soup.select('.content')

#result = soup.find_all('p')
#print(result)
#print(result[0])
#print(type(result))
#print(result.p.string)