# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:54:40 2021

@author: MLZ107
"""

from urllib.request import urlopen

url = 'http://www.baidu.com'

resp = urlopen(url)

# print(resp.read().decode('utf-8'))

with open('mybaidu.html', mode = 'w',encoding = 'utf-8') as f:
    f.write(resp.read().decode('utf-8'))
print('over')

