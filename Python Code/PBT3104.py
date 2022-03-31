# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:32:20 2021

@author: MLZ107
"""

#程序名称：PBT3104.py
#功能：多种类型参数之二
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def print1(str1,x):
    print(str1+"=",end="")
    print(x)
    return

#测试位置参数
def testPositionParms(stdno,name1):
    print1("stdno",stdno)
    print1("name",name1)
    return

#测试默认参数
def testDefaultParms(stdno,name1,grade="2017"):
    print1("stdio",stdno)
    print1("name",name1)
    print1("grade",grade)
    return

#测试关键字参数
def testKeyWordParms(stdno,name1,grade="2017",*,city,zipcode):
    #print1("score",score)
    print1("stdno",stdno)
    print1("name",name1)
    print1("grade",grade)
    print1("city",city)
    print1("zipcode",zipcode)
    return

#测试关键字参数：包裹位置传递
def testVarParms1(*hobby):
    print1("hobby",hobby)
    return

#测试关键字参数：包裹关键字传递
def testVarParms2(**birthplace):
    print1("birthplace",birthplace)
    return

#测试解包裹参数：包裹位置传递
def testUnpackingParms1(basketball,music,reading):
    print1("basketball",basketball)
    print1("music",music)
    print1("reading",reading)
    return

#测试解包裹参数：包裹关键字传递
def testUnpackingParms2(province,city,zipcode):
    print1("province",province)
    print1("city",city)
    print1("zipcode",zipcode)
    return

#测试*args参数与位置参数和默认参数混合应用
def testMixedParms1(stdno,name1,grade="2017",*hobby):
    #print1("score",score)
    print1("stdno",stdno)
    print1("name",name1)
    print1("grade",grade)
    print1("hobby",hobby)
    return

#测试**kwargs与位置参数和默认参数混合应用
def testMixedParms2(stdno,name1,grade="2017",**birthplace):
    #print1("score",score)
    print1("stdno",stdno)
    print1("name",name1)
    print1("grade",grade)
    print1("birthplace",birthplace)
    return

#测试参数复合应用
def testMixedParms3(stdno,name1,grade="2017",*hobby,**birthplace):
     #print1("score",score)
    print1("stdno",stdno)
    print1("name",name1)
    print1("grade",grade)
    print1("hobby",hobby)
    print1("birthplace",birthplace)
    return   

def main():
    print("测试位置参数的应用………")
    x = testPositionParms("201701","李四")
    x = testPositionParms("201702","吴一")
    
    print("测试默认参数的应用……")
    x = testDefaultParms("201701","李四")
    x = testDefaultParms("201702","吴一")
    x = testDefaultParms("201605","西岐")
  
    print("测试关键字参数的应用……")
    x = testKeyWordParms("201701","李四",city="北京",zipcode="100100")
    x = testKeyWordParms("201702","吴一",zipcode="432100",city="孝感")
    
    print("测试可变参数的应用……")
    x = testVarParms1("足球")
    x = testVarParms1("篮球","音乐")
    x = testVarParms1("篮球","音乐","看书")
    x = testVarParms2(province="湖北",city="孝感",zipcode="432100")
    x = testVarParms2(province="上海",city="闵行",zipcode="210000")
    
    print("测试解包裹参数的应用……")
    hobby1=("篮球","音乐","看书")
    x = testUnpackingParms1(*hobby1)
    birthplace1 = {"province":"湖北","city":"孝感","zipcode":"432100"}
    x = testUnpackingParms2(**birthplace1)
    birthplace2 = {"province":"上海","city":"闵行","zipcode":"210000"}
    x = testUnpackingParms2(**birthplace2)
    
    print("测试*args参数与位置参数和魔腾参数混合应用")
    x = testMixedParms1("201702","吴一","2017","篮球","音乐")
    x = testMixedParms1("201605","西岐","2016","政治","娱乐")
    
    print("测试**kwargs与位置参数和默认参数混合应用")
    x = testMixedParms2("201702", "吴一",province="北京",city="大兴",zipcode="102600")
    x = testMixedParms2("201605","西岐","2016",province="北京",city="西域",zipcode="100084")
    
    print("测试参数复合应用……")
    x = testMixedParms3("201701","李四","2017","足球",province="北京",city="大兴",zipcode="102600")
    x = testMixedParms3("201702","吴一","2017","篮球","音乐",province="湖北",city="孝感",zipcode="432100")
    x = testMixedParms3("201703","王五","2017","篮球","音乐","看书",province="上海",city="闵行",zipcode="210000")
    
main()






