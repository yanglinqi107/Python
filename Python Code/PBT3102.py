# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:58:59 2021

@author: MLZ107
"""

#程序名称：PBT3102.py
#功能：参数传递的特点
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def print1(str1,x):
    print(str1+"= ",end="")
    print(x)
    return 1;

def square(x,str1,list1):
    x = x * x
    str1 = "abc"
    list1[0] = list1[0]+1
    return x;

def main():
    x = 3
    str1 = "123"
    list1 = [1,2,3]
    print("调用前……")
    print1("x",x)
    print1("str1",str1)
    print1("list1",list1)
    
    y = square(x,str1,list1)
    print("调用后……")
    print1("y",y)
    print1("x",x)
    print1("str1",str1)
    print1("list1",list1)

main()