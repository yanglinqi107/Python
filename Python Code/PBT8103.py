# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:40:36 2021

@author: MLZ107
"""

#程序名称：PBT8103.py
#功能：文件对象操作
#!/usr/bin/python
#-*- conding:UTF-8-*-

import os
fp = open('myfile','wb')    #以字节的模式创建文件对象
#fp.write(b'里仁为美')      #只能是ASCII字符
#File"<stdin>",line1 
#SyntaxError:bytes can only contain ASCIILiteral characters.
fp.write(b'li ren wei mei')
fp.close()

fp = open("myfile")     #以ASCII字节写入的文件，文件对象可以用文本方式打开
x=fp.read()
print("15.x= ",x)    #b'li ren wei mei'
fp.close()

fp = open('myfile','rb')    #ASCII字节写入的文件，文件对象可以用字节方式打开
x=fp.read()
print("20.x = ",x)  #b'li ren wei mei'
fp.close()

fp = open('myfile','wb')    #创建以字节写的方式的文件对象
#fp.write(b'里仁为美')      #写操作时，只能接收字节参数，使用字符串参数会出错
#File"<stdin>",line1 
#SyntaxError:bytes can only contain ASCIILiteral characters.
fp.write("里仁为美".encode('utf-8'))    #把字符串编码成字节就可以写入
fp.close()

fp = open('myfile','r',encoding = 'utf-8') #在交互模式下，可以使用文本模式打开字节写入的中文字符串
x=fp.read()
print("32.x = ",x)          #'里仁为美'
fp.close()

fp = open('myfile','rb')
x = fp.read()   #每4个符号是一个字节，每3个字节是一个中文
print("37.x = ",x)
fp.tell()
fp.seek(0)  #因为读取文件的时候指针已经去了文件末尾，所以需要移动它到开头
x = fp.read().decode('utf-8') #用字节模式打开文件，查看中文字符需要解码
print("41.x = ",x)
fp.seek(0)
fp.seek(1,1)
x = fp.read()
print("46.x = ",x)
#移动一个字节是不行的，3个字节是一个中文
len1=len("里仁为美")
for i in range(len1):
    fp.seek(3*i)
    x = fp.read()
    print("51.x = ",x)
    print(x.decode("utf-8"))
fp.close()
