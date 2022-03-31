# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:44:37 2021

@author: MLZ107
"""

#程序名称：PBT2402.py
#功能：演示if-elif-else的使用
#!/usr/bin/python
#-* -conding:UTF-8-* -
def main():
    score = int(input("输入分数："))
    if 90 <= score <= 100:
        str1 = "优秀"
    elif 80 <= score <= 89:
        str1 = "良好"
    elif 70 <= score <= 79:
        str1 = "中等"
    elif 60 <= score <= 69:
        str1 = "及格"
    else:
        str1 = "不及格"
    print("成绩为",str1)
    
main()