# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:29:08 2021

@author: MLZ107
"""

#程序名称：PBT7301.py
#功能：自定义异常
#!/usr/bin/python
#-*- conding:UTF-8-*-

class StockError(Exception):
    #com=""     #公司对象
    #amount=0.0     #客户购买产品数
    def __init__(self,com,amount):
        self.com = com
        self.amount = amount
    
    def showExceptionMessage(self,com):
        str1="公司库存="+str(com.stocknum)+"<"+"待购买石油="+str(self.amount)
        return str1
    
class Company:
    #stocknum = 0.0     #库存数量
    def __init__(self,stocknum):
        self.stocknum = stocknum
    
    #产品入库
    def inStock(self,amount):
        if(amount>0.0):
            self.stocknum = self.stocknum + amount
    
    #产品出库
    def outStock(self,amount):
        if(self.stocknum < amount):
            raise StockError(self,amount)
        self.stocknum = self.stocknum - amount
        print("出库成功！！！")
    
    def showStock(self):
        print("公司库存总量="+self.stocknum)
    
try:
    com = Company(10)
    com.inStock(100)
    print("第1次购买")
    com.outStock(100)
    com.inStock(50)
    print("第2次购买")
    com.outStock(80)
except StockError as e:
    print("异常：",e.showExceptionMessage(com))
    
    