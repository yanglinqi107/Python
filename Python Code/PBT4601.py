# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:24:46 2021

@author: MLZ107
"""

#程序名称：PBT4601.py
#功能：栈的应用：表达式括号匹配
#!/usr/bin/python
# -* - conding:UTF-8 -* -

def isLeftBracket(ch):
    if ch in ('(','[','{'):
        return True
    else:
        return False
    
def isRightBracket(ch):
    if ch in (')',']','}'):
        return True
    else:
        return False
    
def toLeftBracket(ch):
    dict1 = {')':'(', ']':'[', '}':'{'}
    return dict1[ch]

#检查表达式中括号是否匹配
#exprs为表达是对应的字符串
#不匹配的情形有以下3种
#情形1：左右括号匹配次序不正确
#情形2：右括号多于左括号
#情形3：左括号多于右括号
def checkMatch(exprs):
    i = 0
    import collections
    stk = collections.deque([])
    while(i<len(exprs)):
        ch = exprs[i:i+1]
        i = i+1
        if(isLeftBracket(ch)):
            stk.append(ch)
        if(isRightBracket(ch)):
            ch1 = toLeftBracket(ch)
            if(len(stk)==0):
                return False;   #情形2
            else:
                ch = stk.pop()
                if(ch!=ch1):
                    return False; #情形1
    if(len(stk)==0):
        return True;
    else:
        return False; #情形3
    
exprs = '[(a+b])*c'
print(checkMatch(exprs))