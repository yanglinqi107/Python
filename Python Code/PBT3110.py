# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 17:15:59 2021

@author: MLZ107
"""

#程序名称：PBT3110.py
#功能：进制转换应用
#!/usr/bin/python
# -* - conding:UTF-8 -* -
import math
def main():
    print("十进制数转换为其他进制数……")
    n = 98
    print(n,"对应的二进制数=",bin(n))
    print(n,"对应的八进制数=",oct(n))
    print(n,"对应的十六进制数=",hex(n))
    
    print("其他进制转换为十进制……")
    #int(s,base)将字符串s表示的base(=2,8,16)进制数组合转化为十进制
    s='111'
    print('二进制数',s,'对应的十进制数=',int(s,2))
    s='567'
    print('八进制数',s,'对应的十进制数=',int(s,8))
    s='123ABC'
    print('十六进制数',s,'对应的十进制数=',int(s,16))
    
    s=str(11111)
    print('二进制数',s,'对应的十进制数=',int(s,2))
    s=str(1356)
    print('八进制数',s,'对应的十进制数=',int(s,8))
    s=str(123)
    print('十六进制数',s,'对应的十进制数=',int(s,16))
    
    print("字符与十进制数之间转换……")
    n=99
    print(n,"对应的ASCII中字符=",chr(n))  #将十进制数n转换为ASCII中相应的字符
    s='W'
    print(s,"对应的十进制数=",ord(s))
    
main()