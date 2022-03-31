# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:49:08 2021

@author: MLZ107
"""

#程序名称：PBT3203.py
#功能：sys模块应用
#!/usr/bin/python
# -* - conding:UTF-8 -* -

import sys
print("命令行参数=",sys.argv)

print("Python版本=",sys.version)
print("模块的搜索路径=",sys.path)

print("操作系统=",sys.platform)
#print("已经导入的模块=",sys.modules.keys())
print("当前正在处理的异常类=",sys.exc_info())

print("最大的Int值=",sys.maxsize)
print("最大的Unicode值=",sys.maxunicode)
print("",sys.modules)

#sys.stdout
#sys.stdin
#sys.stderr