# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:08:06 2021

@author: MLZ107
"""

#程序名称：PBT3109.py
#功能：内置函数的应用
#!/usr/bin/python
# -* - conding:UTF-8 -* -
import math
def main():
    a = float(input('输入三角形边a：'))
    b = float(input('输入三角形边b：'))
    angle = float(input('输入三角形边a和b的夹角:'))
    print("三角形面积=%8.2f"%(a*b*math.sin(angle*math.pi/180)/2))
    
main()