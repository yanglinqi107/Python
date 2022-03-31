# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:25:57 2021

@author: MLZ107
"""

#程序名称：PBT5200.py
#功能：生成序列的几种传统方式
#! /usr/bin/python
#-* -conding:UTF-8 -*-

#方法1
list1 = []
for n in range(10):
    list1.append(2*n**2+3)
print("list1 = ",list1)

#方法2
list3 = [2*n**2+3 for n in range(10)]
print("list3 = ",list3)