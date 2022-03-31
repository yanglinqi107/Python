# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 13:42:22 2021

@author: MLZ107
"""

#程序名称：PBT5103.py
#功能：可迭代对象和迭代器遍历上的差异性
#! /usr/bin/python
#-* -conding:UTF-8 -*-

list1 = [1,2,3,4]
iter1 = iter(list1)
print("2 in iter1 = ",2 in iter1)
print("2 in iter1 = ",2 in iter1)
print("2 in iter1 = ",2 in iter1)
print("2 in iter1 = ",2 in iter1)
print("2 in iter1 = ",2 in iter1)
print("第一次遍历迭代器iter2")
iter2 = iter(list1)
for i in range(1,5):
    print(i,"in iter2 = ",i in iter2)
print("第二次遍历迭代器iter2")
for i in range(1,5):
    print(i,"in iter2 = ",i in iter2)
print("第一次遍历列表list1")
for i in list1:
    print(i,"in list1 = ",i in list1)
print("第二次遍历列表list1")
for i in list1:
    print(i,"in list1 = ",i in list1)