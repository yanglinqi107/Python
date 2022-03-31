# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:57:51 2021

@author: MLZ107
"""

#程序名称：PBT8201.py
#功能：SQLite数据库
#!/usr/bin/python
#-*- conding:UTF-8-*-

import sqlite3

#1.创建表
def createTable(myconn,mycursor,tablename,fieldsTable):
    try:
        sqlstr = 'create table if not exists '+ tablename + fieldsTable
        mycursor.execute(sqlstr)
        myconn.commit()
        return True
    except:
        return False
    
#2.增加记录
def insertRecord(myconn,mycursor,tablename,fieldslist,valueslist):
    try:
        sqlstr = 'insert into '+tablename +fieldslist + ' Values ' + valueslist
        mycursor.execute(sqlstr)
        myconn.commit()
        return True
    except:
        return False

#3.根据条件修改数据库中的数据
def updateRecord(myconn,mycursor,tablename,updateslist,condition):
    try:
        sqlstr = 'update '+tablename+' set '+updateslist+' where '+condition
        mycursor.execute(sqlstr)
        myconn.commit()
        return True
    except:
        return False
    
#4.根据条件删除数据库中的数据
def deleteRecord(myconn,mycursor,tablename,condition):
    try:
        sqlstr = 'delete from '+tablename+' where '+condition
        mycursor.execute(sqlstr)
        myconn.commit()
        return True
    except:
        return False

#5.条件查询
def seekRecord(myconn,mycursor,tablename,condition):
    try:
        sqlstr = 'select * from '+tablename+' where '+condition
        mycursor.execute(sqlstr)
        result = mycursor.fetchall()
        return result
    except:
        return []

#处理开始.....................................................................
myconn=sqlite3.connect('mydatabase3.db')
mycursor = myconn.cursor()

#创建表
tablename = 'scoretable'
#fieldsTable='(stdno text,name text,math int,english int,language int,average int)'
fieldsTable=(
r'(stdno text,'
r'name text,'
r'math int,'
r'english int,'
r'language int,'
r'average int)'
)
createTable(myconn,mycursor,tablename,fieldsTable)

#增加记录
fp=open("mydbfile.txt")
fieldslist='(stdno,name,math,english,language,average)'
for line in fp:
	valueslist='('+line+')'
	insertRecord(myconn,mycursor,tablename,fieldslist,valueslist)
fp.close()
#2.根据条件修改数据库中的数据
updateslist='name="张三丰",english=80'
condition='stdno="9701"'
updateRecord(myconn,mycursor,tablename,updateslist,condition)

#3.根据条件删除数据库中的数据
condition='stdno="9700"'
deleteRecord(myconn,mycursor,tablename,condition)

#4.查询数据库中的数据,以下表为例
#(1)全部查找:
mycursor.execute('select * from '+ tablename)
result=mycursor.fetchall()
print(result)
#(2)根据条件查找:
condition='average>=80'
result=seekRecord(myconn,mycursor,tablename,condition)
print(result)
#(3)数据库模糊查询
'''
模糊查询语句的关键字:like
查询规则:
_x:找到以x结尾,并且x前面只有一个字符的数据,有几个_代表有几个数据
x_:找到以x开头,后面只有一个字符的数据
x%:找到所有以x结束的数据
%x:找到所有以x开头的数据
%x%:找到所有包含x的数据
'''
condition='name LIKE "张%"'
result=seekRecord(myconn,mycursor,tablename,condition)
print(result)

mycursor.close()
myconn.close()
