import requests

proxies = {
    "https":"117.157.197.18:3128"   #"https":"https://117.157.197.18:3128"
}

# url = "https://www.4kbizhi.com/downpic.php?id=8611&fbl=3840x2160"
# headers = {
#     "cookie": "__yjs_duid=1_20261be224677fd5e1071e86f6163fe01636381820696; Hm_lvt_2c6cc9163dcd6f496c48a6b8ac043309=1636381821,1636439542; PHPSESSID=tg2vmejdi1qmfd87p0bb6l4gc0; trennmlusername=qq504612163644; trennmluserid=288923; trennmlgroupid=1; trennmlrnd=l93oV8z7HCQ5BMriVtmZ; trennmlauth=21fee6b6b76d1fec041a8d14530380f1; Hm_lpvt_2c6cc9163dcd6f496c48a6b8ac043309=1636441026",
#     "referer": "https://www.4kbizhi.com/wallpaper/8618-3840x2160.html",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
# }
# resp = requests.get(url = url, headers = headers, proxies = proxies)
# resp.close()
# print(resp.text)

# url = "https://www.4kbizhi.com/e/extend/downpic.php"

# param = {
#     "id": 8321,
#     "fbl": "3840x2160",
#     "t": 0.1081985490788977
# }
# header = {
#     "referer": "https://www.4kbizhi.com/wallpaper/8321-3840x2160.html"
# }
# resp = requests.get(url = url, params = param, proxies = proxies, headers=header)
# resp.close()
# print(resp.json())

url = "https://pic.netbian.com/e/extend/downpic.php"

param = {
    "id": 27301,
    "t": 0.1081985490788977
}
header = {
    "referer": "https://pic.netbian.com/tupian/27301.html"
}
resp = requests.get(url = url, params = param, proxies = proxies, headers=header)
resp.close()
print(resp.json())