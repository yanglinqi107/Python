# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:47:43 2021

@author: MLZ107
"""

#程序名称：PBT6101.py
#功能：类的定义使用初步
#!/usr/bin/python
#-*- conding:UTF-8-*-

class MyBox:
    width = 0.0
    height = 0.0
    def init(self,width1=1.0,height1=1.0):
        self.width = width1
        self.height = height1
        
    def setValue(self,width1,height1):
        self.width = width1
        self.height = height1
        
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height + self.width)
        
def main():
    obj = MyBox()
    print("初始长方形的信息")
    print("width = ",obj.getWidth())
    print("height = ",obj.getHeight())
    obj.setValue(3, 3)
    print("重新设置后长方形的信息")
    print("width = ",obj.getWidth())
    print("height = ",obj.getHeight())
    print("周长 = ",obj.perimeter())
    print("面积 = ",obj.area())
    
main()
        