# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:11:07 2021

@author: MLZ107
"""

#程序名称：PBT5101.py
#功能：Iterable对象判断
#!/usr/bin/python
# -* - conding:UTF-8 -* -

from collections.abc import Iterable
def isIterable():
    print("字符串是Iterable对象否？",isinstance('abc',Iterable))
    list1=[1,2,3]
    print("列表是Iterable对象否？",isinstance(list1,Iterable))
    tup1 = (1,2,3)
    print("元组是Iterable对象否？",isinstance(tup1,Iterable))
    set1 = {1,2,3}
    print("集合是Iterable对象否？",isinstance(set1,Iterable))
    dict1 = {'1':'Jordon','2':'Kobe','3':'James'}
    print("字典是Iterable对象否？",isinstance(dict1,Iterable))
    g = (x for x in range(10))
    #注意(x for x in range(10))为一个generator，因为由列表生成式[]改成了()
    print("generator是Iterable对象否？",isinstance(g,Iterable))
    fname = "abc.txt"
    print("文件是Iterable对象否？",isinstance(fname,Iterable))
    print("数字是Iterable对象否？",isinstance(100,Iterable))
    
def visitIterable():
    s1 = "abc"
    print("遍历输出字符串元素")
    for e in s1:
        print(e,end="")
    print("")
    list1 = [1,2,3]
    print("遍历输出列表元素")
    for e in list1:
        print(e,end="")
    print("")
    tup1 = (1,2,3)
    print("遍历输出元组元素")
    for e in tup1:
        print(e,end="")
    print("")
    set1 = {1,2,3}
    print("遍历输出集合元素")
    for e in set1:
        print(e,end="")
    print("")
    dict1 = {'1':'Jordon','2':'Kobe','3':'James'}
    print("遍历输出字典元素")
    for e in dict1:
        print(e,end="")
    print("")
    fname="Python笔记.txt"
    fp = open(fname,encoding="UTF-8")
    print("遍历输出文件内容")
    for e in fp:
        print(e,end="")
    fp.close()
    
def main():
    isIterable()
    visitIterable()
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    