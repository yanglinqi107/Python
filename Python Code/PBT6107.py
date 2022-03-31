# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:03:16 2021

@author: MLZ107
"""

#程序名称：PBT6107.py
#功能：演示析构函数
#!/usr/bin/python
#-*- conding:UTF-8-*-

class MyClass:
    num = 0
    def __init__(self):
        print("call__init__(self)")
        MyClass.num += 1
        print("num = ",MyClass.num)
        
    def __del__(self):
        print("call__del__(self)")
        if MyClass.num>0 :
            MyClass.num = MyClass.num - 1
        print("num = ",MyClass.num)
        
def main():
    obj1 = MyClass()
    obj2 = MyClass()
    obj3 = MyClass()
    del obj1
    del obj2
    del obj3
    
main()