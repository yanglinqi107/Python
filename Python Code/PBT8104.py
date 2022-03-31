# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:51:24 2021

@author: MLZ107
"""

#程序名称：PBT8104.py
#功能：文件是序列的应用演示
#!/usr/bin/python
#-*- conding:UTF-8-*-

import os
import sys
import codecs
#文件所在目录
print("目前系统的编码为：",sys.getdefaultencoding())

#oldfile:ANSI文件
#newfile:UTF-8文件
#ANSI转换为UTF-8文件
def ANSItoUTF8(oldfile,newfile):
    try:
        fr = open(oldfile,'r',encoding = 'ansi')
        fw = open(newfile,'w',encoding = 'utf-8')
        fread = fr.read()
        fw.write(fread)
        fw.close()
        fr.close()
    except FileNotFoundError as e:
        print(e)

#oldfile:UTF8文件
#newfile:ANSI文件
#UTF8转换为ANSI文件
def UTF8toANSI(oldfile,newfile):
    fr = open(oldfile,'r',encoding = 'utf-8')
    fw = open(newfile,'w',encoding = 'ansi')
    fread = fr.read()
    fw.write(fread)
    fw.close()
    fr.close()
    
fname = 'myfile.txt'
print("文本方式读取文件......")
if(os.path.isfile(fname)):
    fp = open(fname,'r')
    list1 = list(fp)
    print("list1 = ",list1)
    fp.seek(0)
    list2 = fp.readlines()
    print('list2 = ',list2)
    fp.seek(0)
    for line in fp:
        print(line)
    fp.close()
else:
    print(fname,"不存在！！！")

ANSItoUTF8("myfile.txt", "myfileUTF8.txt")
fname = 'myfileUTF8.txt'
print("字节方式读取文件......")
if(os.path.isfile(fname)):
    fp = open(fname,'rb')
    list1 = list(fp)
    print("list1 = ",list1)
    fp.seek(0)
    list2 = fp.readlines()
    print("list2 = ",list2)
    fp.seek(0)
    for line in fp:
        print(line.decode('utf-8'))
    fp.close()
else:
    print(fname,"不存在")
