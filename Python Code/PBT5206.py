# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 20:00:09 2021

@author: MLZ107
"""

#程序名称：PBT5206.py
#功能：生成器的应用：特殊数列
#!/usr/bin/python
#-*- conding:UTF-8-*-

#定义全局变量
maxNum = 10
realNum = 8

def callListExpr():
    #列表生成式
    list1 = [2**(n+1)-1 for n in range(maxNum)]
    print("list1 = ",list1)
    
def callGeneratorExpr():
    #方式1：生成器表达式
    g1 = (2**(n+1)-1 for n in range(maxNum))
    data1 = [next(g1) for n in range(realNum)]
    print("data1 = ",data1)
    
#方式2：生成器函数
#a(n)=p*a(n-1)+q
#假定序列初始两个元素为1
#maxN为最终迭代次数
def fun1(maxN,p,q):
    n,f1 = 0,1
    while n < maxN:
        yield f1
        f1= p*f1+q
        n = n+1
    return "done"

#a(n)=p*a(n-1)+q*a(n-2)
#假定序列初始两个元素为1,1
#maxN为最终迭代次数
def fun2(maxN,p,q):
    n,f0,f1 = 0,1,1
    while n < maxN:
        if n > 0:
            yield f1
            f0,f1 = f1,p*f0+q*f1
        else:
            yield f0
        n = n+1
    return 'done'

#a(n)=p*a(n-1)+q*a(n-2)+w*a(n-3)
#假定序列初始三个元素为1,2,3
#maxN为最终迭代次数
def fun3(maxN,p,q,w):
    n,f0,f1,f2 = 0,1,2,3
    while n < maxN:
        if n==0:
            yield f0
        elif n==1:
            yield f1
        else:
            yield f2
            f0,f1,f2 = f1,f2,p*f0+q*f1+w*f2
        n = n+1
    return 'done'

def main():
    g1 = fun1(maxNum,2,1)
    data1 = [next(g1) for n in range(realNum)]
    print("data1 = ",data1)

    g2 = fun2(maxNum,1,1)
    data2 = [next(g2) for n in range(realNum)]
    print("data2 = ",data2)

    g3 = fun3(maxNum,1,1,1)
    data3 = [next(g3) for n in range(realNum)]
    print("data3 = ",data3)

main()            
