# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:22:43 2021

@author: MLZ107
"""

import requests

query = input("输入查询内容")

url = f"https://www.sogou.com/web?query={query}"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.7.301'
    }

resp = requests.get(url = url, headers = headers)   #处理一个小小的反爬

print(resp.text)

resp.close()