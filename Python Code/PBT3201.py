# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:57:17 2021

@author: MLZ107
"""

#程序名称：PBT3201.py
#功能：模块测试
#!/usr/bin/python
# -* - conding:UTF-8 -* -

#import sys
#sys.paht.append('E:\Python\mymath.py')
import mymath            #引入自定义模块mymath
import random            #引入内置模块random

#以下调用内置模块random中的randint()函数
a = random.randint(1,100)
b = random.randint(1,100)
n = random.randint(1,10)

#以下调用自定义模块mymath中的函数
print("max(",a,",",b,")=",mymath.max(a, b))
print("min(",a,",",b,")=",mymath.min(a, b))
print("sum(",n,")=",mymath.sum(n))
print("mult(",n,")=",mymath.mult(n))

    