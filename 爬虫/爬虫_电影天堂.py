import requests
import re

domain = "https://dytt89.com/"
page = requests.get(url = domain)
#page = requests.get(url = domain, verify = False)
page.encoding = 'gb2312'
#print(page.text)
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<li><a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<href>.*?)"', re.S)
result = obj1.finditer(page.text)
#print(result.__next__().group())
tex = result.__next__().group()
result2 = obj2.finditer(tex)
child_href_list = []
for i in result2:
    child_href = domain + i.group("href").strip("/")
    #print(child_href)
    child_href_list.append(child_href)

for child_href in child_href_list:
    childPage = requests.get(url = child_href)
    childPage.encoding = 'gb2312'
    #print(childPage.text)
    result3 = obj3.search(childPage.text)
    print(result3.group('movie'))
    print(result3.group('href'))

page.close()