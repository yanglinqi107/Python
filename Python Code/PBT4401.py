# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:52:07 2021

@author: MLZ107
"""

#程序名称：PBT4401.py
#功能：集合
#!/usr/bin/python
# -* - conding:UTF-8 -* -

#1、集合创建
def createSet():
    print("集合创建..........................................")
    set1 = {1,2,5,6,7}
    set2 = set()
    set3 = set('abcdef')
    list1 = {"Noah","Jordon","James","Kobe"}
    set4 = set(list1)
    tup1 = ("Noah","Jordon","James","Kobe")
    set5 = set(tup1)
    dict1 = {1:'费德勒',2:'纳达尔',3:'德约科维奇',4:'桑普拉斯'}
    set6 = set(dict1)
    print("set1 = ",set1)
    print("set2 = ",set2)
    print("set3 = ",set3)
    print("set4 = ",set4)
    print("set5 = ",set5)
    print("set6 = ",set6)
    
#2、向集合中添加一个元素s.add()
def addSet():
    set1 = set()
    set1.add(4)
    set1.add(5)
    set1.add(6)
    print("set1 = ",set1)
    
#3、删除元素
def deleteSet():
    #随机删除s.pop()
    set1 = {"Jordon",1,"Kobe",2,"James",3}
    print("删除运算s.pop().....................................")
    print("删除前set1 = ",set1)
    set2 = set1.pop()
    print("删除后set1 = ",set1)
    print("删除后set2 = ",set2)
    
    #指定删除2删除不存在的不会报错s.discard()
    print("删除运算s.discard().....................................")
    print("删除前set1 = ",set1)
    set2 = set1.discard("Kobe")
    set2 = set1.discard("da")
    print("删除后set1 = ",set1)
    
def operateSet():
    #3、集合的交集&，s.intersection()
    set1 = {"Noah","Jordon","James","Kobe"}
    set2 = {"Curry","James","Dulant","Jordon"}
    set12s = set1&set2
    set12m = set1.intersection(set2)
    print("符号运算：set1 ∩ set2 = ",set12s)
    print("函数运算：set1 ∩ set2 = ",set12m)
    
    #4、集合的并集|，s.union()
    set12s = set1|set2
    set12m = set1.union(set2)
    print("并集运算................................................")
    print("set1 = ",set1)
    print("set2 = ",set2)
    print("符号运算：set1 ∪ set2 = ",set12s)
    print("函数运算：set1 ∪ set2 = ",set12m)
    
    #5、集合的差集s1.difference(s2)将集合s1里去掉和s2交集的部分
    set12s = set1 - set2
    set12m = set1.difference(set2)
    print("差集运算...............................................")
    print("set1 = ",set1)
    print("set2 = ",set2)
    print("符号运算：set1 - set2 = ",set12s)
    print("函数运算：set1 - set2 = ",set12m)
    
    #6、集合的交叉补集 s.symmetric_difference()并集里去掉交集的部分
    set12 = set1.symmetric_difference(set2)
    print("交叉补集运算...........................................")
    print("set1 = ",set1)
    print("set2 = ",set2)
    print("set1和set2交叉补集：=",set12)
    
def issubsetTest():
    #7、集合包含关系
    set1 = {"Noah","Jordon","James","Kobe"}
    set2 = {"Curry","James","Dulant","Jordon"}
    set3 = {"James","Jordon"}
    
    print("集合包含关系..........................................")
    print("set1 = ",set1)
    print("set2 = ",set2)
    print("set3 = ",set3)
    print("set1包含set2否？",set2.issubset(set1))
    print("set1包含set3否？",set3.issubset(set1))
    
def main():
    createSet()
    addSet()
    deleteSet()
    operateSet()
    issubsetTest()
    
main()