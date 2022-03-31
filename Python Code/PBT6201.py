# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:11:54 2021

@author: MLZ107
"""

#程序名称：PBT6201.py
#功能：演示类的继承关系
#!/usr/bin/python
#-*- conding:UTF-8-*-

class Researcher:
    def research(self,projecter):
        print("researching......",projecter)
    
    def do(self):
        print("do thing about research each day!")
        
class Person:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
    
    def setvalue(self,height,weight):
        self.height = height
        self.weight = weight
        
    def speak(self):
        print("speaking......")
        
    def do(self):
        print("do something each day!")
    
class Teacher (Person,Researcher):
    def teach(self,course):
        print("teaching......",course)

def main():
    teacher = Teacher(170,66)
    teacher.speak()
    teacher.research("Python")
    teacher.teach("DataStructure")
    print("teacher.height = ",teacher.height)
    print("teacher.weight = ",teacher.weight)
    teacher.setvalue(180,90)
    print("teacher.height = ",teacher.height)
    print("teacher.weight = ",teacher.weight)
    teacher.do()
    Researcher.do(teacher)
    
main()
        
        