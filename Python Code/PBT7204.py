# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:05:57 2021

@author: MLZ107
"""

#程序名称：PBT7204.py
#功能：raise异常举例
#!/usr/bin/python
#-*- conding:UTF-8-*-
#栈：先进先出

import sys
class Teacher:
    def __init__(self,name1="",no1=""):
        self.teachername = name1
        self.teacherno = no1
        
    def teach(self,course):
        print("teaching......",course)
        
print("执行系列语句.......")
try:
    print("可能引起异常语句1......")
    raise IndexError("IndexError")
except IndexError as e:
    print("异常1为：",e)
except Exception as e:
    print("异常为：",e)
except:
    print("There exists Exception!!!")
else:
    print("No Exception!!!")
finally:
    print("Test Exception!!!")
    
print("执行系列语句.......")
try:
    print("可能引起异常语句2......")
    raise AttributeError("AttributeError")
except AttributeError as e:
    print("异常1为：",e)
except Exception as e:
    print("异常为：",e)
except:
    print("There exists Exception!!!")
else:
    print("No Exception!!!")
finally:
    print("Test Exception!!!")
    
print("执行系列语句.......")
try:
    print("可能引起异常语句1......")
    raise IndexError("IndexError")
except IndexError as e:
    print("异常1为：",e)
except Exception as e:
    print("异常为：",e)
except:
    print("There exists Exception!!!")
else:
    print("No Exception!!!")
finally:
    print("Test Exception!!!")
   
print("执行其他语句......")