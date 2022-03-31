# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 16:48:23 2021

@author: MLZ107
"""

import requests

s = input("请输入单词")

data = {"kw":s}

url = 'https://fanyi.baidu.com/sug'

resp = requests.post(url = url, data=data)

print(resp.json())

resp.close()