#程序名称：PBT2202.py
#程序功能：测试列表、元组、集合和字典的定义
#！/usr/bin/python
#-* coding:UTF-8-* -

def testList():
	print("List.........................................................................")
	list1 = [1, 2, 'first', 'second']
	print(type(list1))
	print(list1)
	list2 = [1, 'first', ['first', 'second'], ('冠军', '亚军'), {1, 2, 3}, {1: '优秀',\
2: '良好', 3: '及格', 0: '不及格'}]
	print(type(list2))
	print(list2)
	print(list2[:3])

def testTuple():
    print("Tuple......................................................................")
    tup1 = (1, 2, 'first', 'second')
    print(type(tup1))
    print(tup1)
    tup2 = (1, 'first', ['first', 'second'], ('冠军', '亚军'), {1, 2, 3}, {1: '优秀',\
2: '良好', 3: '及格', 0: '不及格'})
    print(type(tup2))
    print(tup2)
    print(tup2[0:2])
    tup3 = (1,)
    print(tup2[0:1])

def testSet():
	print("Set...........................................................................")
	#set1 = {1, 'first', ['first', 'second'], ('冠军', '亚军'), {1, 2, 3}, {1: '优秀', 2: '良好', 3: '及格', 0: '不及格'}}
	set1 = {1, 'first', ('冠军', '亚军')}
	print(type(set1))
	print(set1)
	set2 = {}
	print(type(set2))
	print(set2)
	#print(set1[0:2])

def testDict():
	print("Dictionary..............................................................")
	dict1 = {1: '优秀', 2: '良好', 3: '及格', 0: '不及格'}
	print(dict1[1])	#输出键为1的值
	print(dict1[2])	#输出键为2的值
	print(dict1)	#输出完整的字典
	print(dict1.keys())	#输出所有键
	print(dict1.values())	#输出所有值
	print(type(dict1))
	dict2 = {1:111, 'str':"字符串", 3:[1, 2, 3], 4:[4 , 5, 6], 5:[7, 8, 9], 6:{1: '优秀', 2:'良好', 3:'及格', 0:'不及格'}}
	print(dict2[1])	#输出键为1的值
	print(dict2['str'])	#输出键为2的值
	print(dict2)	#输出完整的自典
	print(dict2.keys())	#输出所有键
	print(dict2.values/())	#输出所有值
	print(type(dict2))	

def main():
	testList()
	testTuple()
	testSet()
	testDict()
main()


