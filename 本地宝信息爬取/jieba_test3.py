# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:05:10 2021

@author: MLZ107
"""

# 导入包
import jieba
 
#管理系统路径
import sys
sys.path.append("../")
 

 
#导入词性标注的包
import jieba.posseg as pseg
 
#添加词
jieba.add_word('行窃预兆')
jieba.add_word('气定神闲')
 
# 删除词
jieba.del_word('hello')
 
#元组类型的测试数据
test_sent=(
"和深度和等候爱的诶哟广大撒好的坏读书的机会;谁都会厚度啊的哈"
"萨哈帝国画分镜给福建省覅 是否会旁边将发射光谱上方式烧饭"
"[和咯哦安静 ]很烦粉红色会苏粉丝发挥示范是否会四、是服饰"
)
 
# 默认分词
words=jieba.cut(test_sent)
print('/'.join(words))
 
print('*'*40)
 
#用于词性标注
result=pseg.cut('发布时间：2021-05-08 15:10')
 
#使用for 循环把分出的词及其词性用/隔开 并添加空格
for w in result:
    print(w.word,'/',w.flag)
print('\n'+'*'*40)
 
# 对英文的分割
terms=jieba.cut('dha adh d hdsahda adshjah')
print('/'.join(terms))
 
#对英文和汉字的分割
terms=jieba.cut('usdiaiu的埃胡德啊哈的')
print('/'.join(terms))
 
print('*'*40)