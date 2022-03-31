"""
# 版本一
import requests
from bs4 import BeautifulSoup
url = input("输入网址：")
# url = "https://wenku.baidu.com/view/b261fcc6d5bbfd0a795673a9.html"
header = {'User-agent': 'Googlebot'}        # 主要是这个UA，Googlebot，获取到的网页内容和一般UA不一样
res = requests.get(url , headers = header)
res.encoding='gbk'
# print(res.content)
plist = []
soup = BeautifulSoup(res.content, "html.parser")

# txt文件名称
name = soup.find('span', id="doc-tittle-0").text.strip()    # 去空格和换行符
# print(name)
# plist.append(str(soup.title.text))

# 获取文本内容
for div in soup.find_all('div', attrs={"class": "bd doc-reader"}):
    plist.extend(div.get_text().split('\n'))
plist = [c.replace(' ', '') for c in plist]
# plist = [c.replace('\x0c', '') for c in plist]

# 存储到txt文件
file = open(f'E:\\Python\\爬虫_百度文库\\百度文库\\{name}.txt', 'w',encoding='utf-8')
for str in plist:
    file.write(str)
    # file.write('\n')
file.close()
print(name, '保存成功！')
"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 改变了谷歌浏览器的位置，需加上这几行
option = Options()
option.binary_location=r'D:\Program Files\Google\Chrome\Application\chrome.exe'
option.add_argument("--headless")
# url = "https://wenku.baidu.com/view/9d0ed76fae45b307e87101f69e3143323968f5e4.html"
url = input("请输入TXT文件网址：")
driver = Chrome(options = option)
driver.get(url)
page = driver.page_source   # 网页源代码
driver.close()
# print(page)
# charset = re.findall(r'<meta charset="(.*?)">', page)[0]
# print(charset)
soup = BeautifulSoup(page, "lxml")
title = soup.find("h3",attrs={"class":"doc-title"}).text    # 文件名
# print(title)
# for p in soup.find_all("p", attrs={"class":"p-txt"}):
#     print(p)      # p的类型是<class 'bs4.element.Tag'>，写入文件需转换为str
html_head = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>{title}</title>
</head>
<body>    
"""
html_tail = """
</body>
</html>
"""
with open(f"E:\\Python\\爬虫_百度文库\\百度文库\\{title}.html","w",encoding="utf8") as f:
    f.write(html_head)
    for p in soup.find_all("p", attrs={"class":"p-txt"}):
        f.write("   " + str(p))
    f.write(html_tail)
    print(f"{title}.html文件保存完成")