def methodOfDict(n, MyDict):
    for i in range(n):
        ls = input().split()  # 输入命令及参数，之间用空格分隔
        if ls[0] == 'print':  # 每遇到“print”时，在新的一行输出字典
            print(MyDict)
        elif ls[0] == 'key':  # 如果输入的命令是“key”，输出字典中全部键
            print(list(MyDict.keys()))
        elif ls[0] == 'value':  # 如果输入的命令是“value”，输出字典中全部值
            print(list(MyDict.values()))
        elif ls[0] == 'update':  # 如果输入的命令是“update”，更新ls[1]表示的键对应的值
            MyDict[ls[1]] = ls[2]
        elif ls[0] == 'add':  # 如果输入的命令是“add”，增加一个键值对，题目确保输入的键在字典中不存在
            MyDict[ls[1]] = ls[2]
        elif ls[0] == 'del':  # 如果输入的命令是“del”，删除字典中指定的键值对
            if ls[1] not in MyDict:  # 做存在性测试，键不存在时返回“键不存在”
                print('键不存在')
            else:
                del MyDict[ls[1]]  # MyDict.pop(ls[1])
        elif ls[0] == 'clear':  # 如要输入的命令是“clear”，清空字典中全部元素
            MyDict.clear()


if __name__ == '__main__':
    n = int(input())  # 输入一个正整数 n
    name = input().split(',')  # Tom,Jack,Lee
    phoneNumber = input().split(',')  # 13988776655,13855664488,13644668888
    MyDict = dict(zip(name, phoneNumber))  # 以name为键,以phoneNumber为值生成字典
    methodOfDict(n, MyDict)
