import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?kw=saas"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
}
cookies = {
    "Cookie": "_uq=480ca893a7754b67b29317b9c80b0381; uniqid=d01ejtr2yhjfu4; _suq=61d5d3c1-b6e5-4104-a7cb-ee6fb5d2f2a9; _ga=GA1.3.17963389.1636278798; zbj-index-xrzq=1; _ga=GA1.2.17963389.1636278798; local_city_id=3627; local_city_path=wuhan; local_city_name=%E6%AD%A6%E6%B1%89; zbjfeadflow=1; oldvid=6d1737cef07f120e8335e23240929936; vid=454d336abc3bd2414730a1620a323f7b; _gid=GA1.3.873407024.1636425653; Hm_lvt_8e2a01fb7efd931af546fa14cf4187ec=1636278798,1636425653; __utma=168466538.17963389.1636278798.1636278798.1636425654.2; __utmc=168466538; __utmz=168466538.1636425654.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; vidSended=1; Hm_lpvt_8e2a01fb7efd931af546fa14cf4187ec=1636425933; __utmb=168466538.5.10.1636425654; s_s_c=xhA3dh7QsA2lgP8ro4tGR315NCdXH6ZHR%2BRfuGd7ATdHtysboKOI9VU8FzolPihjIJnldq6d%2FaPgx0ltVU14HA%3D%3D"
}

resp = requests.get(url = url, headers = headers, cookies = cookies)
resp.close()
print(resp.text)

html = etree.HTML(resp.text)