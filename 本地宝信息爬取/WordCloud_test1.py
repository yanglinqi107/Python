# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 23:13:17 2021

@author: MLZ107
"""

# -*- coding: utf-8 -*-

from wordcloud import WordCloud, ImageColorGenerator
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image                   # 图片处理
import numpy as np                      # 矩阵运算
 
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
 
mask = np.array(Image.open("back2.png"))
# 生成对象
wc = WordCloud(mask=mask, font_path='msyh.ttc', max_words=200, mode='RGBA', background_color='white')
wc.generate_from_text(string)

# # 从图片中生成颜色
# image_colors = ImageColorGenerator(mask)
# wc.recolor(color_func=image_colors)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
 
# 保存到文件
wc.to_file('wordcloud3.png')