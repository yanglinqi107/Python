# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 15:25:55 2021

@author: MLZ107
"""

#程序名称：PBT8203.py
#功能：MySQL数据库
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#import sqlite3

#1.创建数据库
def  createDatabase(dbname):
	conninfo={'host':'localhost',#默认127.0.0.1
        'user':'root',
        'password':'',
        'port':3306 ,#默认即为3306
        'charset':'utf8'#默认即为utf8
	}
	try:
		myconn = mysql.connector.connect(**conninfo)
		mycursor = myconn.cursor()
		mycursor.execute("CREATE DATABASE"+dbname)
		mycursor.close()
		myconn.close()
		return True
	except:
		return False

#2.连接数据库
#好像连接不成功
def  connectDatabase2(dbname):
	try:
		conn = mysql.connector.connect(
			host ='localhost',
			user ='root',
			password='123456',
			port='3306',
			database=dbname
		)
		return  conn
	except:
		return None

#2.连接数据库
def  connectDatabase(dbname):
	conninfo={'host':'localhost',#默认127.0.0.1
        'user':'root',
        'password':'12345678',
        'port':3306 ,#默认即为3306
        'database':dbname,
        'charset':'utf8'#默认即为utf8
        }
	try:
		conn=mysql.connector.connect(**conninfo)
		return conn
	except mysql.connector.Error as e:
		print('connect fails!{}'.format(e))
		return None

#3.创建表
#mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
def createTable(myconn,mycursor,tablename,fieldsTable):
	try:
		sqlstr='create table '+tablename+fieldsTable
		mycursor.execute(sqlstr)
		myconn.commit()
		return True
	except:
		return False

#4.增加记录
def insertRecord(myconn,mycursor,tablename,fieldslist,valueslist):
	try:
		sqlstr='insert into '+ tablename+fieldslist+' values'+valueslist
		#print("sqlstr",sqlstr)
		mycursor.execute(sqlstr)
		myconn.commit()
		return True
	except:
		return False


#5.根据条件修改数据库中的数据
def updateRecord(myconn,mycursor,tablename,updateslist,condition):
	try:
		sqlstr='update '+ tablename+' set '+updateslist+' where '+condition
		mycursor.execute(sqlstr)
		myconn.commit()
		return True
	except:
		return False


#6.根据条件删除数据库中的数据
def deleteRecord(myconn,mycursor,tablename,condition):
	try:
		sqlstr='delete from '+tablename+' where  '+condition
		mycursor.execute(sqlstr)
		myconn.commit()
		return True
	except:
		return False

#7.条件查询
def seekRecord(myconn,mycursor,tablename,condition):
	try:
		sqlstr='select * from '+ tablename+' where '+condition
		mycursor.execute(sqlstr)
		result=mycursor.fetchall()
		return result
	except:
		return []

def showRowCol(mycursor):
	for col in mycursor.description:       # 显示行描述
		print (col[0], col[1])
	result = mycursor.fetchall()
	for row in result:          # 输出各字段的值
		print (row)
		print (row[1], row[2])

#处理开始.....................................................................
import mysql.connector

dbname='mysqldb'
#createDatabase(dbname)  #创建数据库
myconn = connectDatabase(dbname)  #连接数据库
mycursor = myconn.cursor() #创建游标

#创建表
print("创建表......")

tablename='scoretable'
#tablename='table2'
fieldsTable=(
r'(id int primary key auto_increment,'
r'stdno char(6),'
r'name char(20),'
r'math int,'
r'english int,'
r'language int,'
r'average int);'
)
createTable(myconn,mycursor,tablename,fieldsTable)

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


#根据条件修改数据库中的数据
print("条件修改......")
updateslist='name="张三丰",english=80'
condition='stdno="9701"'
updateRecord(myconn,mycursor,tablename,updateslist,condition)

#根据条件删除数据库中的数据
print("条件删除......")
condition='stdno="9700"'
deleteRecord(myconn,mycursor,tablename,condition)

#查询数据库中的数据,以下表为例
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