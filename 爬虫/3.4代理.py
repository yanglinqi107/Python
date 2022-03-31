import requests

# 117.157.197.18:3128
# url = "https://www.baidu.com"
# proxies = {
#     "https":"117.157.197.18:3128"   #"https":"https://117.157.197.18:3128"
# }

# resp = requests.get(url = url)
# resp.close()
# resp.encoding = 'utf-8'
# print(resp.text)

# resp = requests.get(url = url, proxies = proxies)
# resp.close()
# resp.encoding = 'utf-8'
# print(resp.text)

url = "https://www.baidu.com/s?wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
}
page_text = requests.get(url=url, headers=headers).text

with open('sources/ip.html',mode='w', encoding='utf-8') as f:
    f.write(page_text)
