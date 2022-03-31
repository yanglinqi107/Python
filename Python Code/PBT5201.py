# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 15:32:56 2021

@author: MLZ107
"""

#程序名称：PBT5201.py
#功能：列表生成器
#! /usr/bin/python
#-* -conding:UTF-8 -*-

def showListGenerate():
    list11 = [x*x for x in range(6)]
    print("list11 = ",list11)
    
    list12 = []
    for x in range(6):
        list12.append(x*x)
    print("list12 = ",list12)
    
    list21 = [x*x for x in range(6) if x%2 == 0]
    print("list21 = ",list21)
    
    list22 = []
    for x in range(6):
        if(x%2==0):
            list22.append(x*x)
    print("list22 = ",list22)
    
    list31 = [x*x+y*y for x in range(6)
              for y in range(6) if y%3 == 0]
    print("list31 = ",list31)
    
    list32 = []
    for x in range(6):
        for y in range(6):
            if y%3 == 0:
                list32.append(x*x+y*y)
    print("list32 = ",list32)
    
    list41 = [x*x+y*y for x in range(6) if x%2 == 0
              for y in range(6) if y%3 == 0]
    print("list41 = ",list41)
    
    list42 = []
    for x in range(6):
        if x%2 == 0:
            for y in range(6):
                if y%3 == 0:
                    list42.append(x*x+y*y)
    print("list42 = ",list42)
    
def main():
    showListGenerate()
    
main()