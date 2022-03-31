# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:12:41 2021

@author: MLZ107
"""

#程序名称：PBT5104.py
#功能：Iterator的创建和访问
#! /usr/bin/python
#-* -conding:UTF-8 -*-

import sys
from collections.abc import Iterator
def  visitWithFor():
    #迭代器对象可以使用常规for语句进行遍历
    print("for语句遍历输出字符串中元素.............................")
    s1 = 'abcd'
    iterStr = iter(s1)
    for e in iterStr:
        print(e,end=" ")
    print("")
    
    print("for语句遍历输出列表中元素..............................")
    list1 = [1,2,3,4]
    iterList = iter(list1)
    for e in iterList:
        print(e,end=" ")
    print("")
    
def visitWithNext():
    #使用next()函数遍历
    print("next()函数遍历输出字符串中元素.........................")
    s1 = 'abcd'
    iterStr = iter(s1)
    while True:
        try:
            print(next(iterStr),end=" ")
        except StopIteration:
            break
    print("")
    
    print("next()函数遍历输出列表中元素............................")
    list1 = [1,2,3,4]
    iterList = iter(list1)
    while True:
        try:
            print(next(iterList),end=" ")
        except StopIteration:
            break
    print("")
    
def main():
    visitWithFor()
    visitWithNext()
    
main()