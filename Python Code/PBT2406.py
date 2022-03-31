# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:22:35 2021

@author: MLZ107
"""

#程序名称：PBT2406.py
#功能：演示break对for或while的else语句块的影响
#!/usr/bin/python
# -* - conding:UTF-8 -* -
def main():
    n = 10
    i = 1
    import random
    while i <= n:
        num = random.randint(0, 99)
        if (num % 5 == 0):
            break
        print(num,"不能被5整除")
        i = i + 1
    else:
        print("循环正常终止！！！")
    print("程序结束！！！")
    
main()