# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:04:50 2021

@author: MLZ107
"""

#程序名称：PBT8101.py
#功能：os.paht应用演示
#!/usr/bin/python
#-*- conding:UTF-8-*-

import os
import shutil

def testOsModule():
    print("os.sep=",os.sep)     #取得操作系统特定的路径分隔符
    print("os.name=",os.name)   #指示正在使用的工作平台
    print("os.getcwd()",os.getcwd()) #得到当前工作目录
    print("os.getenv('pythonpath')=",os.getenv("pythonpath")) #读取环境变量
    #print("os.putenv=",os.putenv)      #设置环境变量
    print("os.linesep = ",os.linesep)   #给出当前平台的行终止符
    print("os.listdir()=",os.listdir()) #返回指定目录下的所有文件和目录名
    
def main():
    testOsModule()
main()