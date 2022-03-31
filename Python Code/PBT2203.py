# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:33:53 2021

@author: MLZ107
"""

#程序名称：PBT2203.py
#程序功能：不可变类型的内存分配特点
def main():
    print("赋值变化前......")
    a1=2
    a2=2
    print("id(a1)=",id(a1))
    print("id(a2)=",id(a2))
    
    c1=3+2j
    c2=3+2j
    print("id(c1)=",id(c1))
    print("id(c2)=",id(c2))
    
    s1='good'
    s2='good'
    print("id(s1)=",id(s1))
    print("id(s2)=",id(s2))
    
    tup1=(1,2,3,4)
    tup2=(1,2,3,4)
    print("id(tup1)=",id(tup1))
    print("id(tup2)=",id(tup2))
    
    print("赋值变化后......")
    a1=3
    a2=3
    print("id(a1)=",id(a1))
    print("id(a2)=",id(a2))    
    
    c1=3+4j
    c2=3+4j
    print("id(c1)=",id(c1))
    print("id(c2)=",id(c2))
    
main()