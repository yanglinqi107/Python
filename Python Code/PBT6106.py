# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 19:31:38 2021

@author: MLZ107
"""

#程序名称：PBT6106.py
#功能：演示构造函数
#!/usr/bin/python
#-*- conding:UTF-8-*-

class MyClass:
    num = 0
    def __init__(self):
        print("call__init__(self)")
        self.varx = "123"
        MyClass.num += 1
        print("num = ",MyClass.num)
        
def main():
    obj1 = MyClass()
    obj2 = MyClass()
    obj3 = MyClass()
    print(type(obj1))
    print(type(MyClass))
    obj1.__init__();
    print("obj1.varx = ",obj1.varx)
    #print("MyClass.varx = ",MyClass.varx)
    MyClass.__init__(MyClass)
    print("obj1.varx = ",obj1.varx)
    print("MyClass.varx = ",MyClass.varx)

main()