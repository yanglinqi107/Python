import requests
import re

url = 'https://wenku.baidu.com/view/9a665aa86d1aff00bed5b9f3f90f76c661374cb6.html'
cookies = {
    'kunlunFlag': '1',
    'BIDUPSID': 'C67E33293F1288B5C076AE7E2CC00629',
    'PSTM': '1637390771',
    'BAIDUID': 'C67E33293F1288B53DD58B96286B0682:FG=1',
    'BAIDUID_BFESS': 'C67E33293F1288B53DD58B96286B0682:FG=1',
    '__yjs_duid': '1_8c08191bb53df7546138bab49385111f1637403669927',
    '_click_param_reader_query_ab': '-1',
    'BDUSS': 'EN3ekpHWHZJRlJDbkx2bUFleDd-TVBSTTU4bDBqcVlwcEdWYU9kVkxoT0hGY1JoRVFBQUFBJCQAAAAAAAAAAAEAAAC8P2F4TUxax6fRsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIeInGGHiJxhT',
    'BDUSS_BFESS': 'EN3ekpHWHZJRlJDbkx2bUFleDd-TVBSTTU4bDBqcVlwcEdWYU9kVkxoT0hGY1JoRVFBQUFBJCQAAAAAAAAAAAEAAAC8P2F4TUxax6fRsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIeInGGHiJxhT',
    '__wk_view_topbar_20211030': '1',
    'Hm_lvt_d8bfb560f8d03bbefc9bdecafc4a4bf6': '1637403670,1637648327,1638243609',
    'Hm_lpvt_d8bfb560f8d03bbefc9bdecafc4a4bf6': '1638243609',
    'layer_show_times_by_day_8_c25d171332153dac6a530a90889ac19f': '1',
    'layer_show_times_total_8_c25d171332153dac6a530a90889ac19f': '2',
    'ab_sr': '1.0.1_YTdiMWFmZjg5ZGJiZDRiODk5OWQ3Y2JlMzI4OGJjYjVhNDUzNDg4MThjNDgzNTFiYmVjNWQyMzdlMDI4NjI4OGM3Nzk0ZjY1ZDQ4MWZkMTgwZDdkMzIyODA0ZjM3Yzk2MjlhY2QyYjFiODg1Y2E2ODU5NmY2NWMwYTBmMjY3ODBjMzRkOGNlZDI5NGZmMzdmYjE3NmE4ZmUyMzNjNzI3YWJiOTliNmEyNjM4ZTk2YWM0MTlhZGEyZmNiNjc0OTEx',
    'bcat': '918eadd92e787b0db58a73c5c9c591536cd14bc2b3cc0e886a95c424cfb0d54bc0a52dd74fb2e48747da64eed0acb4af9fd056803837c633e22d038180b604107d76691bac3c73599e094f04589063e0b0e8eeef005e9eb1c42d17dea0756d80ca2407c2a8456264d8f9b2cbeebc4e60036ac13207b4d665181f96f87ba000dc',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

response = requests.get(url=url, headers=headers, cookies=cookies)
response.close()
# print(response.text)

# 标题
title = re.findall(r'<h3 class="doc-title">(.*?)</h3>', response.text, re.S)[0]
# print(title)

# 持久化存储
# with open(f'E:\\Python\\爬虫_百度文库\\百度文库\\{title}.txt', mode='w', encoding='utf-8') as f:
#     f.write(response.text)
#     print('存储完成')


# 200个   0.json? 100个  0.png? 100个   将两个分开存放
json_urls = re.findall(r'"ttf":.*?]},', response.text, re.S)[0]
pageLoadUrl_json = re.findall(r'"pageLoadUrl":"(.*?0.json.*?)"', json_urls, re.S)
# pageLoadUrl_png = re.findall(r'"pageLoadUrl":"(.*?0.png.*?)"', response.text, re.S)  # 有问题，正则又有问题
png_urls = re.findall(r'"png":.*?]},', response.text, re.S)[0]
# print(png_urls)     # 终端输出又不全，改成调试控制台或cmd运行输出
pageLoadUrl_png = re.findall(r'"pageLoadUrl":"(.*?0.png.*?)"', png_urls, re.S)

# print(len(pageLoadUrl_json))   
# for url in pageLoadUrl_json:
#     print(url)

# print(len(pageLoadUrl_png))   
# for url in pageLoadUrl_png:
#     print(url)


# 测试一个url获取的结果，返回的是Unicode编码，需转码
page1 = requests.get(url=pageLoadUrl_json[1])
print(page1.content.decode('unicode-escape', 'ignore'))

# result = ''
# for url in pageLoadUrl_json:
#     page = requests.get(url=url)
#     content = page.content.decode('unicode-escape', 'ignore')
#     items = re.findall(r'"c":"(.*?)".*?"y":(.*?),', content, re.S)
#     y=0
#     for item in items:
#         if not y==item[1]:
#             y=item[1]
#             n='\n'
#         else:
#             n=''
#         result += n
#         result += item[0].strip("\\")
# print(result)


