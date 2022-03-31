# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:56:34 2021

@author: MLZ107
"""

#程序名称：PBT4501.py
#功能：字典应用之一
#!/usr/bin/python
# -* - conding:UTF-8 -* -

#1.创建字典
def createDict():
    print("创建字典.........................................")
    dict1 = {'1':'Jordon','2':'Kobe','3':'James'}
    dict2 = {1:'费德勒',2:'纳达尔',3:'德约科维奇',4:'桑普拉斯'}
    print("dict1 = ",dict1)
    print("dict2 = ",dict2)
    
#2.访问字典里的值
def visitDict():
    print("访问字典里的值....................................")
    dict1 = {'1':'Jordon','2':'Kobe','3':'James'}
    dict2 = {1:'费德勒',2:'纳达尔',3:'德约科维奇',4:'桑普拉斯'}
    print("dict1 = ",dict1)
    print("dict1['1']:",dict1['1'])
    print("dict2 = ",dict2)
    print("dict2[1]:",dict2[1])
    #如果用字典里没有的键访问数据，会输出错误
    #print("dict['4']:",dict1['4'])
    
#3.修改字典
def updateDict():
    print("修改字典.........................................")
    dict1 = {'1':'Jordon','2':'Kobe','3':'James'}
    dict1['3'] = 'LeBron James'
    dict1['4'] = 'Dulant'
    dict1['5'] = 'Curry'
    print("dict1 = :",dict1)
    
#4.删除字典元素
def deleteDict():
    print("删除字典........................................")
    dict1 = {'1':'Jordon','2':'Kobe','3':'James'}
    print("dict1 = ",dict1)
    del dict1['2']
    print("dict1 = :",dict1)
    dict1.clear()
    print("dict1 = :",dict1)
    del dict1
    
def main():
    createDict()
    visitDict()
    updateDict()
    deleteDict()

main()
    