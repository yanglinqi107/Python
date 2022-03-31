# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 21:07:55 2021

@author: MLZ107
"""

#程序名称：PBT7202.py
#功能：多try异常举例
#!/usr/bin/python
#-*- conding:UTF-8-*-

import sys
class Teacher:
    def __init__(self,name1="",no1=""):
        self.teachername = name1
        self.teacherno = no1
        
    def teach(self,course):
        print("teaching......",course)
        
try:
    print("处理可能引起的异常语句1......")
    list1 = [1,2,3,4]
    import random
    i = random.randint(0,10)
    print("list1[",i,"]",list1[i])
    a = random.randint(0,20) - 10
    b = random.randint(0,20) - 10
    c = a / b
    print(a,"/",b,"= ",c)
    teacher = Teacher()
    print("teacher.sex = ",teacher.sex)
    
except IndexError as e:
    print("异常1=",e)
except AttributeError as e:
    print("异常2=",e)
except ZeroDivisionError as e:
    print("异常3=",e)
except Exception as e:
    print("异常4=",e)
except:
    print("There exists Exception!!!")
else:
    print("No Exception!!!")
finally:
    print("Test Exception!!!")

print("执行完部分语句，又遇到一些可能引起异常的语句")

try:
    print("处理可能引起的异常语句1......")
    for i in range(10):
        print("i = ",i)
    num = input("输入数字：")
    int(num)
    dic = {'name':'egon'}
    dic['age']

except TypeError as e:
    print("异常5=",e)
except ValueError as e:
    print("异常6=",e)
except KeyError as e:
    print("异常7=",e)
except Exception as e:
    print("异常8=",e)
except:
    print("There exists Exception!!!")
else:
    print("No Exception!!!")
finally:
    print("Test Exception!!!")
    
print("处理其他语句.......")