# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:54:58 2021

@author: MLZ107
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

tokens=[ 'my','dog','has','flea','problems','help','please',
         'maybe','not','take','him','to','dog','park','stupid',
         'my','dalmation','is','so','cute','I','love','him'  ]
#统计词频
freq = nltk.FreqDist(tokens)
 
#输出词和相应的频率
for key,val in freq.items():
    print (str(key) + ':' + str(val))
 
#可以把最常用的5个单词拿出来
standard_freq=freq.most_common(5)
print(standard_freq)
 
#绘图函数为这些词频绘制一个图形
freq.plot(20, cumulative=False)

#去除停用词
clean_tokens=tokens[:]
stwords=stopwords.words('english')
for token in tokens:
    if token in stwords:
        clean_tokens.remove(token)
print(clean_tokens)

#分句
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext))

#分词
from nltk.tokenize import word_tokenize
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(word_tokenize(mytext))

#标记非英语语言文本
from nltk.tokenize import sent_tokenize
mytext = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."
print(sent_tokenize(mytext,"french"))

#词干提取
from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('working'))
#结果为：work 
from nltk.stem import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
print(lancaster_stemmer.stem('working'))
#结果为：work 

#提取非英语单词词干
from nltk.stem import SnowballStemmer
print(SnowballStemmer.languages)
#结果为：('danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish')

french_stemmer = SnowballStemmer('french')
print(french_stemmer.stem("French word"))
#结果为：french word