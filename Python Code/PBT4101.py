# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:19:03 2021

@author: MLZ107
"""
#程序名称：PBT4101.py
#功能：字符串格式化：%格式化
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def main():
    name1 = input("输入姓名：")
    age1 = int(input("输入年龄："))
    score1 = float(input("输入分数："))
    #1.不指定width和precision
    sf = "name=%s,age=%d,score=%f"
    print(sf%(name1,age1,score1))
    #2.指定width和precision
    sf = "name=%15s,age=%5d,score=%8.2f"
    print(sf%(name1,age1,score1))
    #3.指定占位符宽度（左对齐）
    sf = "name=%-15s,age=%5d,score=%8.2f"
    print(sf%(name1,age1,score1))
    #4.指定占位符（只能用0当占位符？）
    sf = "name=%-15s,age=%05d,score=%08.2f"
    print(sf%(name1,age1,score1))
    #5.选择指定的key
    sf = "name=%(name)s,age=%(age)d,score=%(score)f"
    print(sf%{'name':name1,'age':age1,'score':score1})
    
main()