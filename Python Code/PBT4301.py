# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 13:54:04 2021

@author: MLZ107
"""

#程序名称：PBT4301.py
#功能：元组
#!/usr/bin/python
# -* - conding:UTF-8 -* -

#1、元组创建
def createTuple():
    print("元组创建.....................................")
    tup1 = (1,2,3,4,5)
    tup2 = "a","b","c","d"  #无括号也可以
    print("tup2 = ",tup2)
    tup3 = ()
    print("tup3 = ",tup3)
    tup4 = (50,)
    print("tup4 = ",tup4)
    tup5 = tuple('abcdef')
    print("tup5 = ",tup5)
    list1 = ["Jordon",1,"Kobe",2,"James",3]
    tup6 = tuple(list1)
    print("tup6 = ",tup6)
    set1 = {"Jordon",1,"Kobe",2,"James",3}
    tup7 = tuple(set1)
    print("tup7 = ",tup7)
    dict1 = {1:'费德勒',2:"纳达尔",3:"德约科维奇",4:"桑普拉斯"}
    tup8 = tuple(dict1)
    print("tup8 = ",tup8)
    
#2、元组截取
def sliceTuple():
    print("元组截取.....................................")
    tup1 = ("Jordon",1,"Kobe",2,"James",3)
    print("tup1[0] = ",tup1[0])
    print("tup1[1:5] = ",tup1[1:5])
    
#3、元组运算符
#元组连接
def addTuple():
    print("元组连接.....................................")
    tup1 = ("Noah","Jordon","James","Kobe")
    tup2 = ("Curry","James","Dulant","Jordon")
    tup3 = tup1 + tup2
    print("tup1 = ",tup1)
    print("tup2 = ",tup2)
    print("tup1 + tup2 = ",tup3)
    
#元组复制
def repeatTuple():
    print("元组复制.............................................")
    tup1 = ("Curry","James")
    tup2 = tup1*3
    print("tup1 = ",tup1)
    print("tup1 * 3 = ",tup2)
    
#判断某元素是否属于元组
def inTuple():
    print("判断某元素是否属于元组.................................")
    tup1 = ("Noah","Jordon","James","Kobe")
    print("Curry属于tup1否？","Curry" in tup1)
    print("James属于tup1否？",'James' in tup1)

def mathTuple():
    #1、len(tuple):计算元组元素个数
    tup1 = ("Noah","Jordon","James","Kobe")
    print("元组tup1 = ",tup1)
    print("元组tup1的长度=",len(tup1))
    #2、max(tuple):返回元组中元素最大值
    print("元组tup1的最大值 = ",max(tup1))
    #3、返回元组中元素最小值
    print("元组tup1的最小值 = ",min(tup1))
    
def main():
    createTuple()
    sliceTuple()
    addTuple()
    repeatTuple()
    inTuple()
    mathTuple()
    
main()
    
            
    