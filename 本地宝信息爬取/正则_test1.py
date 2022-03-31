# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:46:40 2021

@author: MLZ107
"""

import re
s = '武汉wh,wofj我的'
pattern = re.compile('\w') 
match = pattern.match(s)
print(match.group())