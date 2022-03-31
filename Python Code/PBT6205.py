# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:40:39 2021

@author: MLZ107
"""

#程序名称：PBT6205.py
#功能：抽象方法
#!/usr/bin/python
#-*- conding:UTF-8-*-

import abc
class Peoples(metaclass = abc.ABCMeta):
    @ abc.abstractmethod
    def speak(self):
        pass
    
    @ abc.abstractmethod
    def eat(self):
        pass
    
class Chinese(Peoples):
    def speak(self):
        print("中国人用中文交流！！！")
        
    def eat(self):
        print("中国人吃放用筷子！！！")
    
class American(Peoples):
    def speak(self):
        print("美国人用英文交流！！！")
    
    def eat(self):
        print("美国人吃放用刀叉！！！")
        
class Japanese(Peoples):
    def speak(self):
        print("日本人用日语交流！！！")
        
    def eat(self):
        print("日本人吃放用刀叉或筷子！！！")
        
def main():
    chinese = Chinese()
    american = American()
    japanese = Japanese()
    chinese.speak()
    chinese.eat()
    american.speak()
    american.eat()
    japanese.speak()
    japanese.eat()
    
main()