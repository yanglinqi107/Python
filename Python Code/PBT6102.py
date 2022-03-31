# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 11:24:55 2021

@author: MLZ107
"""

#程序名称：PBT6102.py
#功能：成员变量的访问
#!/usr/bin/python
#-*- conding:UTF-8-*-

class Researcher:
    workno = '123'
    def publish(self,str1):
        self.author = str1
        temp = 0
        print("成员变量author属于：",str1)
        
def main():
    print("Researcher.workno = ",Researcher.workno)
    researcher = Researcher()
    print("researcher.workno = ",researcher.workno)
    print("Researcher.workno = ",Researcher.workno)
    researcher.workno="20050000"
    print("researcher.workno = ",researcher.workno)
    print("Researcher.workno = ",Researcher.workno)
    
    Researcher.publish(Researcher,"类Researcher")
    print("Researcher.author = ",Researcher.author)
    researcher.publish("对象researcher")
    print("researcher.author = ",researcher.author)
    
main()
    