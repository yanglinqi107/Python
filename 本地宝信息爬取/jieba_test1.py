# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:19:20 2021

@author: MLZ107
"""

# -*- coding: utf-8 -*-
import jieba

seg_str = "好好学习，天天向上。"

print("/".join(jieba.lcut(seg_str)))    # 精简模式，返回一个列表类型的结果
print("/".join(jieba.lcut(seg_str, cut_all=True)))      # 全模式，使用 'cut_all=True' 指定 
print("/".join(jieba.lcut_for_search(seg_str)))     # 搜索引擎模式
result = jieba.cut(seg_str)
print(result)
print(type(result))

txt = open("E:\Python\Class BigWork\武汉人才引进政策.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(20):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
    


def get_text():
    txt = open("本地宝城市网址.txt", "r", encoding='UTF-8').read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")      # 将文本中特殊字符替换为空格
    return txt

file_txt = get_text()
words = file_txt.split()    # 对字符串进行分割，获得单词列表
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1 

items = list(counts.items())    
items.sort(key=lambda x: x[1], reverse=True)      

for i in range(5):
    word, count = items[i]
    print("{0:<5}->{1:>5}".format(word, count))