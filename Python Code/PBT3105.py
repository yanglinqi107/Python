# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:21:37 2021

@author: MLZ107
"""

#程序名称：PBT3105.py
#功能：lambda表达式
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def main():
    #lambda表达式无名称的使用
    print("lambda表达式无名称的使用")
    list1 = [1,2,3,4,5,6,7,8,9]
    print(list(map(lambda x:x*x,list1)))
    
    #lambda表达式有名称的使用
    print('lambda表达式有名称的使用')
    fun1 = lambda x,y:x*x+y*y           #命名lambda表达式为fun1
    print(fun1(1,2))                    #像函数一样调用
    
    #lambda表达式作为列表的元素
    print('lambda表达式作为列表的元素')
    list2 = [(lambda x:x*x),(lambda x,y:x*y),(lambda x,y,z:x*y*z)]
    print(list2[0](2),list2[1](2,3),list2[2](2,3,4))
    
    #lambda表达式中调用函数
    print('lambda表达式中调用函数')
    list3 = [25,18,15,18,13,10,26,26,10,12]
    list4 = list(map(lambda x:(x-min(list3))/(max(list3)-min(list3)),list3))
    print("list4 = ",list4)
    
main()
    