# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:46:32 2021

@author: MLZ107
"""

#程序名称：PBT4602.py
#功能：利用队列打印二项式系数
#!/usr/bin/python
# -* - conding:UTF-8 -* -

def printBipoly(n):
    e1 = 0
    e2 = 0
    import collections
    que = collections.deque([])
    que.append(1)
    que.append(1)
    print("",end="")
    for k in range(2*n+1):
        print("",end="")
    print("{:3d}".format(1),end="")
    print("")
    for i in range(1,n+1):
        print("",end="")
        for k in range(2*n-i+1):
            print("",end="")
        que.append(0);
        for k in range(1,i+3):
            e1 = que.popleft()
            que.append(e1+e2)
            e2=e1
            if(k!=(i+2)):
                print("{:3d}".format(e2),end="")
        print("")
        
printBipoly(5)