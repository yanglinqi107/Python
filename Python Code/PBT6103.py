# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:53:05 2021

@author: MLZ107
"""

#程序名称：PBT6103.py
#功能：私有变量和公共变量
#!/usr/bin/python
#-*- conding:UTF-8-*-

class MyStudent:
    __classidea = "勤奋"      #班级理念
    totalnum = 0             #统计班级人数
    classno = "201700"       #班级编号
    def __init__(self):
        self.stdno = ""
        self.stdname = ""
        self.__stdDiseaseStatus = ""
        MyStudent.totalnum = MyStudent.totalnum + 1
        
    def setStudentInfo(self,no1,name1,status1):
        self.stdno = no1
        self.stdname = name1
        self.__stdDiseaseStatus = status1
        
    def setClassInfo(idea1,no1):
        MyStudent.__classidea = idea1
        MyStudent.classno = no1
        
    def getClassIdea():
        return MyStudent.__classidea
    
    def getDiseaseStatus(self):
        return self.__stdDiseaseStatus

def main():
    print("class.__classidea = ",MyStudent.getClassIdea())
    print("class.totalnum = ",MyStudent.totalnum)
    print("class.classno = ",MyStudent.classno)
    
    MyStudent.setClassInfo("勤奋好学","201701")
    print("class.__classidea = ",MyStudent.getClassIdea())
    print("class.totalnum = ",MyStudent.totalnum)
    print("class.classno = ",MyStudent.classno)
    
    obj1 = MyStudent()
    obj1.setStudentInfo("20170101", "张三", {"高血压"})
    print("class.totalnum = ",MyStudent.totalnum)
    print("object.stdno = ",obj1.stdno)
    print("object.stdname = ",obj1.stdname)
    print("object.__stdDiseaseStatus = ",obj1.getDiseaseStatus())
    
    obj2 = MyStudent()
    obj2.setStudentInfo("20170102", "里斯", {"高血压","胃病"})
    print("class.totalnum = ",MyStudent.totalnum)
    print("object.stdno = ",obj2.stdno)
    print("object.stdname = ",obj2.stdname)
    print("object.__stdDiseaseStatus = ",obj2.getDiseaseStatus())
    
main()
        