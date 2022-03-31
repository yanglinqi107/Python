# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:49:07 2021

@author: MLZ107
"""

#程序名称：PBT5203.py
#功能：生成器的定义方式演示
#! /usr/bin/python
#-* -conding:UTF-8 -*-

maxNum = 10
realNum = 8
list1 = [2*n**2+3 for n in range(maxNum)]
print("list1 = ",list1)

#方式1：生成器表达式
g1 = (2*n**2+3 for n in range(maxNum))
data1 = [next(g1) for n in range(maxNum)]
print("data1 = ",data1)

#方式2：生成器函数
def createData(maxN):
    n = 0
    while n < maxN:
        an = 2*n**2+3
        yield an
        n = n+1

g2 = createData(maxNum)
data2 = [next(g2) for n in range(realNum)]
print("data2 = ",data2)