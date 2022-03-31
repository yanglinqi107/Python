# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:20:07 2021

@author: MLZ107
"""

#程序名称：PBT5202.py
#功能：生成器
#! /usr/bin/python
#-* -conding:UTF-8 -*-

def showGenerator():
    #列表生成式
    list1 = [2*n**2+3 for n in range(10)]
    print("list1 = ",list1)
    
    #生成器生成式
    maxNum = 10
    g1 = (2*n**2+3 for n in range(maxNum))
    realNum = 8
    data1 = [next(g1) for n in range(realNum)]
    print("data1 = ",data1)
    
    #列表生成式
    list2 = [x*x+y*y for x in range(5) for y in range(3)]
    print("list2 = ",list2)
    
    #生成器生成式
    maxRaws = 5
    maxCols = 3
    realNum = 8
    g2 = (x*x+y*y for x in range(maxRaws) for y in range(maxCols))
    realNum = 8
    data2 = [next(g2) for n in range(realNum)]
    print("data2 = ",data2)
    
def main():
    showGenerator()
    
main()