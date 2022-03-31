# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 12:20:53 2021

@author: MLZ107
"""

def main():
    import random
    quit = 1
    qNum = 0
    tNum = 0
    while(quit != 0 and quit == 1):
        preNum = random.randrange(0,10,1)
        postNum = random.randint(0,9)
        sum = preNum + postNum
        print(preNum,"+",postNum,"=",end="")
        sum1 = int(input())
        if sum == sum1:
            print("正确")
            tNum += 1
        else:
            print("错误，结果=",sum)
        qNum += 1
        print("继续：1，结束：0",end="")
        quit = int(input())
        print()
    s = float(tNum)/qNum*100
    print("共答",qNum,"题，答对",tNum,"题，正确率为%.2f"%s,"%")
main()