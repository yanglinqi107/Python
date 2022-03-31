# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 14:24:19 2021

@author: MLZ107
"""

#程序名称：PBT4104.py
#功能：字符串
#!/usr/bin/python
# -* - conding:UTF-8 -* -

def createStr():
    #1、字符串创建
    print("字符串创建.......................")
    str1 = '12567'
    str2 = ''
    list1 = ["Noah","Jordon","James","Kobe"]
    str3 = str(list1)
    tup1 = ("Noah","Jordon","James","Kobe")
    str4 = str(tup1)
    set1 = {"Noah","Jordon","James","Kobe"}
    str5 = str(set1)
    print("str1 = ",str1)
    print("str2 = ",str2)
    print("str3 = ",str3)
    print("str4 = ",str4)
    print("str5 = ",str5)

def operateStr():
    #字符串运算
    #+：字符串连接
    print("+：字符串连接...................")
    str1 = '123'
    str2 = 'abc'
    str3 = str1+str2
    print("str1 = ",str1)
    print("str2 = ",str2)
    print("str3 = ",str3)
    
def repeatStr():
    #*：重复输出字符串
    print("*：重复输出字符串......................")
    str1 = "abc"
    str2 = str1*2
    print("str1 = ",str1)
    print("str2 = ",str2)
    
def sliceStr():
    #[]:通过索引获取字符串中的字符
    #[:]：截取字符串中的一部分
    print("*索引与切片...........................")
    str1 = "0123456789"
    print("str1[0:3] = ",str1[0:3])         #截取第一位到第三位的字符
    print("str1[:] = ",str1[:])             #截取字符串的全部字符
    print("str1[6:] = ",str1[6:])           #截取第七个字符到结尾
    print("str1[:-3] = ",str1[:-3])         #截取从头开始到倒数第三个字符之前
    print("str1[2] = ",str1[2])             #截取第三个字符
    print("str1[-1] = ",str1[-1])           #截取倒数第一个字符
    print("str1[::-1] = ",str1[::-1])       #创造一个与原字符串顺序相反的字符串
    print("str1[-3:-1] = ",str1[-3:-1])     #截取倒数第三位与倒数第一位之前的字符
    print("str1[-3:] = ",str1[-3:])         #截取倒数第三位到结尾
    print("str1[:-5:-3] = ",str1[:-5:-3])   #逆序截取
    
def inStr():
    #in:成员运算符：如果字符串中包含给定的字符返回True
    print("in:成员运算符.............................")
    str1 = 'abcdef'
    print("a在字符串str1中否？","a" in str1)
    print("cd在字符串str1中否？","cd" in str1)
    print("g在字符串str1中否？","g" in str1)
    
def othersStr():
    #字符串常见方法
    print("字符串常见方法.......................")
    #1、去掉空格和特殊符号
    #s.strip():去掉空格和换行符
    print("a bcd ef.strip()=","a bdc ef".strip())
    #s.strip('xx'):去掉某个字符串
    str1 ='abcdabef'
    print(str1+".strip('ab') = ",str1.strip('ab'))
    #s.lstrip():去掉左边的空格和换行符
    #s.rstrip():去掉右边的空格和换行符
    #2、字符串的搜索和替换
    #s.count('x'):查找某个字符在字符串里面出现的次数
    print(str1+".count('a') = ",str1.count('a'))
    #s.capitalize():首字母大写
    #s.center(n,'-'):把字符串放中间，两边用-对齐
    #s.find('x'):找到这个字符返回下标，多个时返回第一个；不存在返回-1
    print(str1+".find('c') = ",str1.find("c"))
    print(str1+".find('g') = ",str1.find('g'))
    #s.index('x'):找到这个字符返回下标，多个时返回第一个；不存在的字符返回-1
    print(str1+".index('b') = ",str1.index('b'))
    #s.replace(oldstr,newstr):字符串替换
    print(str1+".replace('ab','Java') = ",str1.replace('ab','Java'))
    #3、字符串的测试和替换函数
    #s.startswith(prefix[,start[,end]])：是否以prefix开头
    #s.endswith(suffix[,start[,end]])：以suffix结尾
    #s.isalnum()：是否全是字母和数字，并至少有一个字符
    #s.isalpha()：是否全是字母，并至少有一个字符
    #s.isdigit()：是否全是数字，并至少有一个字符
    #s.isspace()：是否全是空白字符，并至少有一个字符
    #s.islower()：s中的字母是否全是小写
    #s.isupper()：s中的字母是否全是大写
    #s.istitle()：s是否是首字母大写的
    
def splitStr():
    #4、字符串分割
    print("字符串分割......................")
    str2 = 'Noah Jordon James Kobe'
    #s.split():默认是按照空格分割
    print(str2+".split() = ",str2.split())
    #s.split(','):按照逗号分割
    str2 = 'Noah,Jordon,James,Kobe'
    print(str2+".split(',') = ",str2.split(','))
    str2 = 'Noah*Jordon*James*Kobe'
    print(str2+".split('*') = ",str2.split('*'))
    str2 = 'Noah*#Jordon*#James*#Kobe'
    print(str2+".split('*#') = ",str2.split('*#'))
    
def joinStr():
    #5、字符串连接
    print("字符串连接........................")
    list1 = ['This','is','Python']
    print("join= ",','.join(list1))
    print("join= ",'-'.join(list1))
    print("join= ",'*'.join(list1))
    print("join= ",'##'.join(list1))

def showStringModule():
    #6、string模块
    print("string模块应用........................")
    import string 
    print("所有大写字母=",string.ascii_uppercase)
    print("所有小写字母=",string.ascii_lowercase)
    print("所有字母=",string.ascii_letters)
    print("所有数字=",string.digits)
    
def main():
    createStr()
    operateStr()
    sliceStr()
    inStr()
    othersStr()
    splitStr()
    joinStr()
    showStringModule()
    
main()