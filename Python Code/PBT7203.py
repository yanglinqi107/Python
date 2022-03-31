# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 10:45:59 2021

@author: MLZ107
"""

#程序名称：PBT7203.py
#功能：raise异常举例
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
    import random
    i = random.randint(0,6)
    if i == 1:
        raise IndexError("IndexError")
    elif i == 2:
        raise AttributeError("AttributeError")
    elif i == 3:
        raise ZeroDivisionError("ZeroDivisionError")
    elif i == 4:
        raise Exception("Exception")
    else:
        print("不抛出异常！！！")

except IndexError as e:
    print("异常1为：",e)
except AttributeError as e:
    print("异常2为：",e)
except ZeroDivisionError as e:
    print("异常3为：",e)
except Exception as e:
    print("异常4为：",e)
except:
    print("There exists Exception!!!")
else:
    print("No Exception!!!")
finally:
    print("Test Exception!!!")
print("处理其他事情！！！")
