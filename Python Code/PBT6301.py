# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:04:57 2021

@author: MLZ107
"""

#程序名称：PBT6301.py
#功能：演示自定义类及其如何使用
#!/usr/bin/python
#-*- conding:UTF-8-*-

class MyVector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def setVector(self,x,y):
        self.x = x
        self.y = y
        
    #向量相加
    def addVector(self,v1,v2):
        self.x = v1.x + v2.x
        self.y = v1.y + v2.y
        
    #向量相减
    def minusVector(self,v1,v2):
        self.x = v1.x - v2.x
        self.y = v1.y - v2.y
        
    #向量内积
    def multVector(self,v1):
        return self.x*v1.x+self.y*v1.y
    
    def showVector(self,str1):
        print(str1,"=<",self.x,",",self.y,">")
        
def main():
    vect1 = MyVector(1, 2)
    vect2 = MyVector(3, 4)
    vect3 = MyVector(5, 6)
    vect1.showVector("vect1")
    vect2.showVector("vect2")
    vect3.addVector(vect1, vect2)
    vect3.showVector("vect3")
    vect3.minusVector(vect1, vect2)
    vect3.showVector("vect3")
    
main()