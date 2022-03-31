# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:55:26 2021

@author: MLZ107
"""

#程序名称:PBT2204.py
#程序功能:可变类型的内存分配特点
def main():
    #多次赋值给同一变量
    list1 = [1,2,3]
    print("id(list1)=",id(list1))
    list1 = [1,2,3]
    print("id(list1)=",id(list1))
    list1 = [1,2,3]
    print("id(list1)=",id(list1))
    
    #赋值给不同变量
    list1 = [1,2,3]
    list2 = [1,2,3]
    print("id(list1)=",id(list1))
    print("id(list1[0])=",id(list1[0]))
    print("id(list1[1])=",id(list1[1]))
    print("id(list1[2])=",id(list1[2]))
 
    print("id(list2)=",id(list2))
    print("id(list2[0])=",id(list2[0]))
    print("id(list2[1])=",id(list2[1]))
    print("id(list2[2])=",id(list2[2]))
main()