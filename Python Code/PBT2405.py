# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:16:53 2021

@author: MLZ107
"""

#程序名称：PBT2405.py
#功能：演示break应用
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def main():
    n = 50
    i = 1
    while i <= n:
        if (i % 5 == 0):
            break
        print(i,"不能被5整除")
        i = i + 1
    
main()