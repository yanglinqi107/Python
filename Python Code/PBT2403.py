# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:04:28 2021

@author: MLZ107
"""

#程序名称：PBT2403.py
#功能：演示for循环应用
#!/usr/bin/python
# -* -conding:UTF-8 -* -
def main():
    n = 20
    m = 5
    sum = 0
    for i in range(0,n+1):
        if (i%m==0):
            sum += i
    print("sum = ",sum)

main()            