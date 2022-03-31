# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 19:29:17 2021

@author: MLZ107
"""

#程序名称：PBT5205.py
#功能：send()方法演示
#!/usr/bin/python
#-*- conding:UTF-8-*-

def gen():
    a = yield 1
    print("a = ",a)
    b = yield 2
    print("b = ",b)
    c = yield 3
    print("c = ",c)
    return "It is over"

g= gen()
print("*******************************")
n1 = g.send(None)
print("第1个yield参数值为：",n1)
print("*******************************")
n2 = g.send("The 2st send")
print("第2个yield参数值为：",n2)
print("*******************************")
n3 = g.send("The 3rd send")
print("第3个yield参数值为：",n3)
print("*******************************")

try:
    n4 = g.send("The 4st send")
except StopIteration:
    print("运行到末尾了，没有yield语句供继续运行！")
finally:
    print("*********************************")