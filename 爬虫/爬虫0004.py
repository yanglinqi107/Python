# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 17:22:03 2021

@author: MLZ107
"""

import requests

url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
    }

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
    }
resp = requests.get(url = url, params=param, headers = header)

#print(resp.request.url)

#print(resp.request.headers)

#print(resp.text)

print(resp.json())

resp.close()