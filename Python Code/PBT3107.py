# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:31:54 2021

@author: MLZ107
"""

#程序名称：PBT3107.py
#功能：reduce()函数
#!/usr/bin/python
# -* - conding:UTF-8 -* -

from functools import reduce

#计算阶乘 n!
def mult(x,y):
    return x*y

#计算 f(n)=nf(n-1)+n**3,f(0)=1
def fun1(fv,n):
    return n*fv+n**3

def main():
    print("计算阶乘 n!")
    result = reduce(mult,[1,2,3,4,5,6,7,8,9])
    print("result = ",result)
    
    print("计算f(n) = nf(n-1)+n**3")
    result = reduce(fun1,[1,2,3,4,5],1)
    print("result = ",result)
    
main()