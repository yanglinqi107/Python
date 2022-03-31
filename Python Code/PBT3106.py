# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:23:05 2021

@author: MLZ107
"""

#程序名称：PBT3106.py
#功能：map()函数
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def main():
    #与lambda表达式配套使用
    print('与lambda表达式配套使用')
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = list(map(lambda x:x*x, list1))
    print('lsit2 =',list2)
    
    #与自定义函数配套使用
    print('与自定义函数配套使用')
    def squareSum(x,y):
        return x*x+y*y
    
    list3 = [16,10,25,28,25,14,28,20,15,17]
    list4 = [24,28,15,26,20,24,23,16,29,25]
    list5 = list(map(squareSum, list3,list4))
    print('list5 = ',list5)
    
main()