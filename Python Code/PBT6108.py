# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:14:26 2021

@author: MLZ107
"""

#程序名称：PBT6108.py
#功能：类的变量和方法增加、删除
#!/usr/bin/python
#-*- conding:UTF-8-*-

class MyStudent:
    classno = "201701"
    def __init__(self,stdname="",stdno="",sex=""):
        self.stdname = stdname
        self.stdno = stdno
        self.sex = sex
        
    def printInfo(self):
        print("stdname = ",self.stdname)
        print("stdno = ",self.stdno)
        print("sex = ",self.sex)
    
    def setInfo(self,stdname,stdno,sex):
        self.stdname = stdname
        self.stdno = stdno
        self.sex = sex
    
    def testDel(self):
        print("删除前stdname = ",self.stdname)
        del self.stdname
        #print("删除前stdname = ",self.stdname)
        self.stdname = "珊珊"
        print("删除后又增加stdname = ",self.stdname)
        
    def showClassIdea():
        print("MyStudent.classidea = ",MyStudent.classidea)
        
    def callFunCls1(str1):
        MyStudent.funCls1(str1)
        
def main():
    obj = MyStudent()
    obj.printInfo()
    obj.setInfo("张三", "1701", "女")
    obj.printInfo()
    #del obj.stdname
    #obj.printInfo()
    #obj.setInfo("张三","1701","女")
    #obj.printInfo()
    obj.testDel()
    #MyStudent.showClassIdea()
    MyStudent.classidea="勤奋好学"
    MyStudent.showClassIdea()
    
    #增加实例方法
    def funObject1(self,str1):
        print("Object = ",self," 方法= ",str1)
    #动态绑定对象
    obj.funObj1 = funObject1
    #调用绑定方法
    #Python不会自动将调用者绑定到第一个参数
    #因此程序需要手动将调用者绑定为第一个参数
    obj.funObj1(obj,"funObj1")
    
    #增加非实例方法
    def funClass1(str1):
        print("方法=",str1)
    #动态绑定方法到类
    MyStudent.funCls1 = funClass1
    MyStudent.funCls1("类外调用MyStudent.funCls1")
    MyStudent.callFunCls1("类内调用MyStudent.funCls1")
    
main()
        