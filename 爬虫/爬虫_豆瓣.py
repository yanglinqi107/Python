import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
}
page = requests.get(url = url, headers = headers)
#print(page.text)
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<div class="bd">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)
result = obj.finditer(page.text)
#写到csv文件中
fp = open("data.csv",mode='w')
csvwriter = csv.writer(fp)
for i in result:
    # print(i.group("name"))
    # print(i.group("year").strip())
    # print(i.group("score"))
    # print(i.group("num"))
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values()) 
fp.close()
page.close()
print("over!")