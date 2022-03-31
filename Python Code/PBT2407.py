# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:27:29 2021

@author: MLZ107
"""

#程序名称：PBT2407.py
#功能：演示continue应用
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def main():
    n = 50
    i = 1
    while i <= n:
        if (i % 5 == 0):
            continue
        print(i,"不能被5整除")
        i = i + 1
    
main()