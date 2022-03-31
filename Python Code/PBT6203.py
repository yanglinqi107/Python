# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:09:33 2021

@author: MLZ107
"""

#程序名称：PBT6203.py
#功能：演示构造方法的继承
#!/usr/bin/python
#-*- conding:UTF-8-*-

class Researcher:
    def __init__(self,jobtitle = '工程师'):
        self.jobtitle=jobtitle
        
    def setJobtitle(self,jobtitle):
        self.jobtitle = jobtitle
        
    def research(self,projecter):
        print("researching......",projecter)
    
    def do(self):
        print("do thing about research each day!")
        
    def publish(self,str1):
        print("Researcher发表内容：",str1)
        
class Person:
    def __init__(self,height = 0,weight = 0):
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
    teacher = Teacher()
    print("teacher.height = ",teacher.height)
    print("teacher.weight = ",teacher.weight)
    teacher.setvalue(180,90)
    print("teacher.height = ",teacher.height)
    print("teacher.weight = ",teacher.weight)
    #print("teacher.jobtitle = ",teacher.jobtitle)
    teacher.setJobtitle("高工")
    print("teacher.jobtitle = ",teacher.jobtitle)
    
main()
        
        