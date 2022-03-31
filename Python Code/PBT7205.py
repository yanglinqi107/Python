# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:16:27 2021

@author: MLZ107
"""

#程序名称：PBT7205.py
#功能：自定义异常
#!/usr/bin/python
#-*- conding:UTF-8-*-

class ScoreError(Exception):
    def __init__(self,score):
        self.score = score
    
    def __str__(self):
        return self.score

def inputScore():
    score = int(input("输入分数[0,100]:"))
    if score <= 0 or score >= 100:
        raise ScoreError("分数错：分数应位于区间[0,100]!!!")
        
try:
    inputScore()
except ScoreError as e:
    print("异常=",e)
except:
    print("There exists Exception!!!")
else:
    print("No Exception!!!")
finally:
    print("异常测试结束。")
