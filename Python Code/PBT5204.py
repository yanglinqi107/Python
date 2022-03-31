# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:03:12 2021

@author: MLZ107
"""

#程序名称：PBT5204.py
#功能：next()和_next()_方法演示
#!/usr/bin/python
#-*- conding:UTF-8-*-

def gen():
    a = yield 1
    b = yield 2
    return 100

g1 = gen()
n1 = next(g1)
print("n1 = ",n1)
n2 = next(g1)
print("n2 = ",n2)

g2 = gen()
n3 = g2.__next__()
print("n3 = ",n3)
n4 = g2.__next__()
print("n4 = ",n4)