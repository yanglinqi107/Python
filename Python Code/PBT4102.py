# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:54:10 2021

@author: MLZ107
"""

#程序名称：PBT4102.py
#功能：字符串格式化：format
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def main():
    stdname = input("输入姓名：")
    age = int(input("输入年龄："))
    score = float(input("输入分数："))
    #1.使用参数位置格式
    print("1.使用参数位置格式")
    sf = "stdname={0},age={1},score={2}"
    print(sf.format(stdname,age,score))
    list1=[stdname,age,score]
    print(sf.format(*list1))
    tup1 = (stdname,age,score)
    print(sf.format(*tup1))
    
    #2.使用参数名
    print("2.使用参数名")
    sf = "stdname={stdname},age={age},score={score}"
    print(sf.format(stdname=stdname,age=age,score=score))
    dict1={'stdname':stdname,'age':age,'score':score}
    print(sf.format(**dict1))
    
    #3.设置格式化的输出宽度、填充、对齐方式
    print("3.设置格式化的输出宽度、填充、对齐方式")
    sf = "stdname={0:*<10},age{1:*<10},score={2:*<10}"
    print(sf.format(stdname,age,score))
    sf="srdname={0:*^10},age={1:*^10},score={2:*^10}"
    print(sf.format(stdname,age,score))
    sf="srdname={0:*>10},age={1:*>10},score={2:*>10}"
    print(sf.format(stdname,age,score))
    
    #4.设置输出格式：宽度和小数位
    print("4.设置输出格式：宽度和小数位")
    sf = "stdname={0:15s},age={1:5d},score={2:8.2f}"
    print(sf.format(stdname,age,score))
    sf = "stdname={0:15s},age={1:05d},score={2:08.2f}"
    print(sf.format(stdname,age,score))
    
main()