# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:21:22 2021

@author: MLZ107
"""

#程序名称：PBT4201.py
#功能：列表应用：基本操作
#!/usr/bin/python
# -* - conding:UTF-8 -* -

def createList():
    #1、列表创建
    print("列表创建........................")
    list1 = [1,2,3,4,5]
    print("list1 = ",list1)
    list2=[]
    list3=list('agcdef')
    print("list3 = ",list3)
    tup1 = ("Jordon",1,"Kobe",2,"James",3)
    list4 = list(tup1)
    print("list4 = ",list4)
    set1 = {"Jordon",1,"Kobe",2,"James",3}
    list5 = list(set1)
    print("list5 = ",list5)
    dict1 = {1:'费德勒',2:'纳达尔',3:'德约科维奇',4:'桑普拉斯'}
    list6 = list(dict1)
    print("list6 = ",list6)
    
def sliceList():
    #2、列表截取
    print("列表截取........................................")
    list1 = ["Jordon",1,"Kobe",2,"James",3]
    print("list1[0] = ",list1[0])
    print("list1[1:5] = ",list1[1:5])
    
def addList():
    #3、列表运算符
    #列表连接+
    print("列表连接............................")
    list1 = ["Noah","Jordon","James","Kobe"]
    list2 = ["Curry","James","Dulant","Jordon"]
    list3 = list1 + list2
    print("list1 = ",list1)
    print("list2 = ",list2)
    print("list1+list2 = ",list3)
    
def repeatList():
    #元素复制
    print("列表复制...................................")
    list1 = ["Curry","James"]
    list2 = list1*3
    print("list1 = ",list1)
    print("list1*3 = ",list2)
    
def updateList():
    #元素修改
    print("列表修改....................................")
    list1 = ["Noah","Jordon","James","Kobe"]
    list1[2]='LeBron James'
    print("list1 = ",list1)
    
def inList():
    #判断某元素是否属于列表
    print("判断某元素是否属于列表.......................")
    list1 = ["Noah","Jordon","James","Kobe"]
    print("Curry属于list否？",'Curry' in list1)
    print("James属于list1否？",'James' in list1)
    
def mathList():
    #1、len(listle):计算列表元素个数
    list1 = ["Noah","Jordon","James","Kobe"]
    print("列表list1= ",list1)
    print("列表list1的长度 = ",len(list1))
    #2、max(listle):返回列表中元素最大值
    print("列表list1的最大值 = ",max(list1))
    #3、min(listle):返回列表中元素最小值
    print("列表list1的最小值 = ",min(list1))
    
def main():
    createList()
    sliceList()
    addList()
    repeatList()
    updateList()
    inList()
    mathList()
    
main()