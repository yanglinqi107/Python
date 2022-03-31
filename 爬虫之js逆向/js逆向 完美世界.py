# url = 'https://passport.wanmei.com/login?location=L3NhZmUv'

import execjs
from lxml import etree
import requests

url = 'https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53",
    "Referer": "https://passport.wanmei.com/login?location=L3NhZmUv"
}
resp_text = requests.post(url=url, headers=headers).text
tree = etree.HTML(resp_text)
key = tree.xpath('//input[@id="e"]/@value')[0]
# print(key)
node = execjs.get()
ctx = node.compile(open('E:\\Js\\完美世界.js','r', encoding='gbk').read())
funcName = 'getPwd("{0}","{1}")'.format('123456',key)
pwd = ctx.eval(funcName)
print(pwd)
