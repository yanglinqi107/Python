# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:06:09 2021

@author: MLZ107
"""

#程序名称：PBT4105.py
#功能：字符串应用二
#!/usr/bin/python
# -* - conding:UTF-8 -* -

#//将串s2插入到串s1的第i个字符后面
def insertStr(s1,s2,i):
    return s1[0:,i]+s2+s1[i,len(s1)]
#删除串s中第i个字符开始的连续j个字符
def deleteStr(s,i,j):
    return s[0:i-1]+s[i+j-1:len(s)]
#从串s1中删除所有和串s2相同的子串
def deleteStrAll(s1,s2):
    s0 = ""
    len2 = len(s2)
    j = s1.find(s2)
    #print("s1= "+s1+" s2= "+s2+" j= "+j)
    while(j>=0):
        s0 = deleteStr(s1,j+1,len2)
        #print("s1= "+s1+" s0="+s0)
        s1 = s0
        j = s1.find(s2)
    return s0

str1 = "abcabefabgha"
str2 = "ab"
print("str1 = ",str1)
print("str2 = ",str2)
print("deleteStrAll(str1,str2) = ",deleteStrAll(str1,str2))
#可以直接用替换
print(str1.replace(str2, ""))
