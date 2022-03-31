import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url = url)
resp.encoding = 'utf-8'
#print(resp.text)

resp.close()

main_page = BeautifulSoup(resp.text, 'html.parser')
result = main_page.find('div', class_ = 'TypeList')
#print(result)
result = result.find_all('a')
#print(result)
href_list = []
for i in result:
    #print(i['href'])
    href_list.append("https://www.umei.cc" + i.get('href'))

img_src_list = []
for i in href_list:
    resp = requests.get(url = i)
    resp.encoding = 'utf-8' 
    resp.close()
    child_page = BeautifulSoup(resp.text, 'html.parser')
    result = child_page.find("div", class_="ImageBody")
    result = result.find('img')
    img_src_list.append(result['src'])
    time.sleep(1)

for src in img_src_list:
    img_resp = requests.get(url = src)
    #img_resp.content的字节
    img_name = src.split('/')[-1]
    with open('img/' + img_name, mode='wb') as f:
        f.write(img_resp.content)
    print("over!")
    time.sleep(1)

print("over!!!")



