# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:40:40 2021

@author: MLZ107
"""

#程序名称：PBT6202.py
#功能：演示类的继承关系：覆盖
#!/usr/bin/python
#-*- conding:UTF-8-*-


class Researcher:
    def research(self,projecter):
        print("researching......",projecter)
    
    def do(self):
        print("do thing about research each day!")
        
    def publish(self,str1):
        self.author = str1
        print("Researcher发表内容：",str1)
        
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
        
    def do(self):
        print("do teaching each day!")
        
    def publish(self):
        print("Teacher发表内容为教学成果！！！")

def main():
    teacher = Teacher(170,66)
    teacher.do()
    Researcher.do(teacher)
    Person.do(teacher)
    teacher.publish()
    #teacher.publish("项目或系统")
    Researcher.publish(teacher,"项目或系统1")
    #print("Teacher.author = ",Teacher.author)
    Researcher.publish(Teacher,"项目或系统2")
    print("Teacher.author = ",Teacher.author)
    #teacher1 = Teacher(170,66)
    print("teacher.author = ",teacher.author)
    
main()
        
        