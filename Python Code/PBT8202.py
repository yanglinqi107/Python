# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:06:36 2021

@author: MLZ107
"""

#程序名称：PBT8202.py
#功能：Access数据库
#!/usr/bin/python
#-*- conding:UTF-8-*-
#import sqlite3

import os
import pypyodbc

#1.创建表
#mycursor.execute('CREATE TABLE t1(id COUNTER PRIMARY KEY,name CHAR(25));').commit()
def createTable(myconn,mycursor,tablename,fieldsTable):
    try:
        sqlstr = 'create table '+tablename+fieldsTable
        mycursor.execute(sqlstr)
        myconn.commit()
        return True
    except:
        return False
    
#2.增加记录
def insertRecord(myconn,mycursor,tablename,fieldslist,valueslist):
    try:
        sqlstr = 'insert into '+tablename+fieldslist+' values'+valueslist
        #print("sqlstr",sqlstr)
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

def mdb_conn(dbname,password=""):
    '''
    功能：创建数据库连接
    :param dbname:数据库名称
    :param password:数据库密码，默认为空
    :return:返回数据库连接
    '''
    str1 ='Driver={Microsoft Access Driver (*.mdb)};PWD='+password+";DBQ="+dbname
    conn = pypyodbc.win_connect_mdb(str1)
    return conn

def showRowCol(mycursor):
    for col in mycursor.description:
        print(col[0],col[1])
    result = mycursor.fetchall()
    for row in result:
        print(row)
        print(row[1],row[2])

dbname='E:\Python\mydb1.mdb'
#createDatabase(dbname)   #创建一个新的Access数据库
myconn=mdb_conn(dbname)  #连接数据库
mycursor = myconn.cursor()   #产生cursor游标
#创建表
tablename='scoretable'
fieldsTable=(
r'(id COUNTER PRIMARY KEY,'
r'stdno CHAR(6),'
r'name CHAR(25),'
r'math int,'
r'english int,'
r'language int,'
r'average int);'
)
#createTable(myconn,mycursor,tablename,fieldsTable)

#增加记录
print("增加记录......")
fp=open("mydbfile2.txt")
fieldslist='(stdno,name,math,english,language,average)'
for line in fp:
	valueslist='('+line+')'
	insertRecord(myconn,mycursor,tablename,fieldslist,valueslist)
fp.close()

#result=mycursor.execute("select * from scoretable")
#print('70.result=',result)
#showRowCol(mycursor)


#2.根据条件修改数据库中的数据
print("条件修改......")
updateslist='name="张三丰",english=80'
condition='stdno="9701"'
updateRecord(myconn,mycursor,tablename,updateslist,condition)

#3.根据条件删除数据库中的数据
print("条件删除......")
condition='stdno="9700"'
deleteRecord(myconn,mycursor,tablename,condition)

#4.查询数据库中的数据,以下表为例
#(1)全部查找:
print("查询全部......")
mycursor.execute('select * from '+ tablename)
result=mycursor.fetchall()
print(result)
#(2)根据条件查找:
print("条件全部......")
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
print("模糊查询......")
condition='name LIKE "张%"'
result=seekRecord(myconn,mycursor,tablename,condition)
print(result)