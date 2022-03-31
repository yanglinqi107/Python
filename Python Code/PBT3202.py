# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:38:46 2021

@author: MLZ107
"""

#程序名称：PBT3202.py
#功能：内置模块的应用
#!/usr/bin/python
# -* - conding:UTF-8 -* -
import math
import random
def main():
    r1 = random.random()
    r2 = random.random()
    e1 = math.sqrt(-2*math.log(r1))*math.cos(2*math.pi*r2)
    e2 = math.sqrt(-2*math.log(r1))*math.sin(2*math.pi*r2) 
    print("第一个随机价格变量值=%6.2f"%(1500+150*e1))
    print("第二个随机价格变量值=%6.2f"%(1500+150*e2))
    print("价格P的模拟值=%6.2f"%(1500+150*(e1+e2)/2))
    
main()