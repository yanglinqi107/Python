# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:49:45 2021

@author: MLZ107
"""

#程序名称：PBT3108.py
#功能：函数递归
#!/usr/bin/python
# -* - conding:UTF-8 -* -

#sum(n) = 1+2+...+n
def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n
    
#mult(n)=1*2*...*n
def mult(n):
    if n==1 or n==0:
        return 1
    else: 
        return mult(n-1)*n
    
#fibonacci数:1,1,2,3,5,8...
def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def main():
    n = int(input("输入n: "))
    print("sum(",n,") =",sum(n))
    print("mult(",n,") =",mult(n))
    print("fibonacci(",n,") =",fibonacci(n))

main()