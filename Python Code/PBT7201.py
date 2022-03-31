# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 20:54:15 2021

@author: MLZ107
"""

#程序名称：PBT7201.py
#功能：异常举例
#!/usr/bin/python
#-*- conding:UTF-8-*-

import sys
class Teacher:
    def __init__(self,name1="",no1=""):
        self.teachername = name1
        self.teacherno = no1
        
    def teach(self,course):
        print("teacher......",course)
        
try:
    list1 = [1,2,3,4]
    import random
    i = random.randint(0,10)
    print("list1[",i,"] = ",list1[i])
    a = random.randint(0,20) - 10
    b = random.randint(0,20) - 10
    c = a / b
    print(a,"/",b,"=",c)
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
    print("No Expception!!!")
finally:
    print("Test Exception!!!")

print("处理其他事情！！！")