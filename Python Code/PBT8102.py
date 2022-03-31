# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:12:38 2021

@author: MLZ107
"""

#程序名称：PBT8102.py
#功能：os.path应用演示
#!/usr/bin/python
#-*- conding:UTF-8-*-

import os
import time

def testOspathModule():
    #[1]返回path规范化的绝对路径
    print(os.path.abspath("PBT8102.py"))
    
    #[2]将path分割成目录和文件名二元组返回
    print(os.path.split("E:\Python\PBT8102.py"))
    
    #[3]返回path的目录。其实就是os.path.split(path)的第一个元素
    print(os.path.dirname("E:\Python\PBT8102.py"))
    
    #[4]返回path最后的文件名。如果path以/或\结尾，那么就会返回空值
    print(os.path.basename("E:\Python\"PBT8102.py"))
    
    #[5]返回list中，所有path共有的最长的路径
    #pritn(os.path.commonprefix(list))
    
    #[6]如果path存在，返回True，否则返回False
    print(os.path.exists("E:/Python"))
    
    #[7]如果path是绝对路径，返回True
    print(os.path.isabs("E:/Python"))
    
    #[8]如果path是一个存在的文件，返回True，否则返回False
    print(os.path.isfile("PBT8102.py"))
    
    #[9]如果path是一个存在的目录，返回True，否则返回False
    print(os.path.isdir("E:/Python"))
    
    #[12]返回(drivername,fpath)元组
    print(os.path.splitdrive("E:/Python"))
    
    #[13]分离文件名与扩展名，默认返回(fname,fextension)元组，可做分片操作
    print(os.path.splitext("PBT8102.py"))
    
    #[14]返回path的文件的大小（字节）
    print(os.path.getsize("PBT8102.py"))
    
    #[15]返回path所指向的文件或者目录的最后存取时间
    print(os.path.getatime("PBT8102.py"))
    
    #[16]返回path所指向的文件或者目录的最后修改时间
    print(os.path.getmtime("PBT8102.py"))
    
def main():
    testOspathModule()
main()