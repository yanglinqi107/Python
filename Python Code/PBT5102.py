# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:20:35 2021

@author: MLZ107
"""

#程序名称：PBT5102.py
#功能：Iterator对象判断
#! /usr/bin/python
#-* -conding:UTF-8 -*-
from collections.abc import Iterator
def isIterator():
    s1 = 'abc'
    print("字符串是Iterator对象否？",isinstance(s1,Iterator))
    list1 = [1,2,3]
    print("列表式Iterator对象否？",isinstance(list1,Iterator))
    tup1 = (1,2,3)
    print("元组是Iterator对象否？",isinstance(tup1,Iterator))
    set1 = {1,2,3}
    print("集合是Iterator对象否？",isinstance(set1,Iterator))
    dict1 = {'1':'Jordon','2':'Kobe','3':'James'}
    print("字典是Iterator对象否？",isinstance(dict1,Iterator))
    g = (x for x in range(10))
    #注意(x for x in range(10))为一个generator，因为由列表生成式[]改成了()
    print("generator是Iterator对象否？",isinstance(g,Iterator))
    fname = "abc.txt"
    print("文件是Iterator对象否？",isinstance(fname,Iterator))
    print("数字是Iterator对象否？",isinstance(100,Iterator))
    
def main():
    isIterator()
    
main()