# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:09:00 2021

@author: MLZ107
"""

#程序名称：PBT2404.py
#!/usr/bin/python
# -* -conding:UTF-8-*-
def main():
    n = 20
    m = 5
    sum = 0
    i = 1
    while i <= n:
        if (i % m == 0):
            sum += i
        i = i + 1
    print("sum = ",sum)

main()