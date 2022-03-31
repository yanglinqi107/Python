# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 19:03:53 2021

@author: MLZ107
"""

#程序名称：mymath.py
#功能：自定义函数模块

#返回x和y的较大值
def max(x,y):
    if x>y:
        return x
    else:
        return y

#返回x和y的较小值
def min(x,y):
    if x<y:
        return x
    else:
        return y

#返回1+2+……+n的值
def sum(n):
    sum0 = 0
    for i in range(1,n+1):
        sum0 += i
    return sum0

#返回n!=1*2*……*n的值
def mult(n):
    mult0 = 1
    for i in range(1,n+1):
        mult0 *= i
    return mult0