import requests

# 会话
session = requests.session()

url = "https://passport.17k.com/ck/user/login"

data = {
    "loginName": "",
    "password": ""
}

resp = session.post(url = url, data = data)
resp.close()
print(resp.text)
# print(resp.cookies)

url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
resp = session.get(url = url)
resp.close()
print(resp.json())

headers = {
    "Cookie": "GUID=42da01a5-1451-4d5d-8407-4ba9e71363be; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F07%252F47%252F79%252F85137947.jpg-88x88%253Fv%253D1636430804000%26id%3D85137947%26nickname%3DYLQ107%26e%3D1651983168%26s%3D5b08c142d37d528d; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2285137947%22%2C%22%24device_id%22%3A%2217d02c6765f8b9-0e98652b92d265-561a1053-1327104-17d02c67660679%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2242da01a5-1451-4d5d-8407-4ba9e71363be%22%7D"
}

resp = requests.get(url = url, headers = headers)
resp.close()
print(resp.json())