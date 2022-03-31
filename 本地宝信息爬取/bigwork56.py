# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 20:32:01 2021

@author: MLZ107
"""

import jieba                            # 分词
from matplotlib import pyplot as plt    # 绘图，数据可视化
from wordcloud import WordCloud         # 词云
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运算
import jieba.posseg as pseg        #导入词性标注的包
import jieba.analyse

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False
            
txt = open("E:\Python\Class BigWork\武汉人才引进政策.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数
for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    elif word.isdigit():
        continue
    elif is_chinese(word):
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序
word_list=[]
for i in range(30):
    # if(items[i][0].isdigit() or items[i][0].isalpha):
    #     continue
    word_list.append(items[i][0])
string = ' '.join(word_list)
#print(string)    

# for i in range(20):
#     word, count = items[i]
#     print("{0:<5}{1:>5}".format(word, count))
    
img = Image.open('back.png')   # 打开遮罩图片
img_array = np.array(img)   # 将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc",    # 字体所在位置：C:\Windows\Fonts
    #最大号字体
    max_font_size=200,
    height = 400,
    width = 400
)
wc.generate_from_text(string) 
wc.to_file('WorldCould.png')

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()