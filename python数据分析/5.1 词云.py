# ------------      -------    --------    -----------    -----------
# @File       : 10.4.3 词云实验模板.py
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/27 23:53
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------

import string
import re
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串，只保留文件中的英文字母和西文符号，过滤掉中
    文，所有字符转为小写，将其中所有标点、符号替换为空格，返回字符串。"""
    # =======================================================
    with open(file, 'r', encoding='utf-8') as f:
        # re.findall(r'[a-zA-Z]+', f.read(), re.I | re.S)
        ret = re.findall('[a-zA-Z]+', f.read(), re.S)
    ret = ' '.join(ret)
    return ret.lower()
    # =======================================================


def word_frequency(txt):
    """
    @参数 txt：去除标点、符号的文本，字符串
    接收去除标点、符号的字符串，统计并返回每个单词出现的次数。返回值为字典类型，单词为键，对
    应出现的次数为值。"""
    # =======================================================
    lst = txt.split()
    word_dic = {}
    for word in lst:
        if word in word_dic.keys():
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return word_dic
    # =======================================================


def draw_cloud_en_freq(en_frequency):
    """
    @参数 en_frequency：词频，字典类型
    绘制词云，传入参数为词频，设定图片的宽度600，高度400，背景白色、字体最大值150、
    图片边缘为5。
    """
    # =======================================================
    wc = WordCloud(
        width=600,  # 设置图片的宽度
        height=400,  # 设置图片的高度
        background_color='White',  # 设置背景颜色
        max_font_size=150,  # 设置字体最大值
        margin=5,  # 设置图片的边缘
    )
    wc.generate_from_frequencies(en_frequency)
    plt.imshow(wc)  # 负责对图像进行处理，并显示其格式，但是不能显示。
    plt.axis("off")  # 不显示坐标轴
    # wc.to_file('dream.png')                   # 词云保存为图片
    plt.show()  # 显示图像
    # =======================================================


def draw_cloud_en_txt(text):
    """
    @参数 text：读文件获取的文本，字符串
    绘制词云，传入参数为文本(字符串)，设定图片的宽度600，高度400，背景白色、字体最大值150、
    图片边缘为5。"""
    # =======================================================
    wc = WordCloud(
        width=600,  # 设置图片的宽度
        height=400,  # 设置图片的高度
        background_color='White',  # 设置背景颜色
        max_font_size=150,  # 设置字体最大值
        margin=5  # 设置图片的边缘
    )
    wc.generate(text)
    plt.imshow(wc)  # 负责对图像进行处理，并显示其格式，但是不能显示。
    plt.axis("off")  # 不显示坐标轴
    plt.show()
    # =======================================================


def read_file_cn(file):
    """接收文件名为参数，将文件中的内容读为字符串"""
    # =======================================================
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    return text
    # =======================================================


def word_frequency_cn(txt):
    """
    @参数 txt：读文件获取的文本，字符串
    传入参数为读文件获取的文本字符串。jieba.analyse.textrank()可用参数topK设置最多返回多少个按
    词频降序排列的关键词列表，数据格式为列表：[('人民', 1.0), ('中国', 0.9533997295396189), ...]
    将列表转为字典:{'人民': 1.0, '中国': 0.9533997295396189,...}，返回这个字典,字典的键是关键词，
    值是关键词的权值。"""
    # =======================================================
    result = jieba.analyse.textrank(txt, topK=60, withWeight=True)
    word = dict()
    for i in result:  # 遍历列表，生成字典
        word[i[0]] = i[1]
    return word  # 返回词与权值字典
    # =======================================================


def draw_cloud_cn(frequency_dict):
    """
    @参数 frequency_dict：词频，字典类型
    接收词频字典为参数，用'ball.jpg'做词云背景。利用matplotlib中的imread('ball.jpg')从图像文件读
    入数据,得到一个表示图像的NumPy数组。"""
    # =======================================================
    graph = plt.imread('ball.jpg')
    wc = WordCloud(
        font_path='msyh.ttc',  # 中文字体
        background_color='White',  # 设置背景颜色
        mask=graph,  # 设置背景图片
        max_font_size=240  # 设置字体最大值
    )
    wc.generate_from_frequencies(frequency_dict)
    plt.imshow(wc)  # 对图像进行处理
    plt.axis("off")  # 不显示坐标轴
    # wc.to_file('dream.png')                   # 词云保存为图片
    plt.show()  # 显示图像
    # =======================================================


if __name__ == '__main__':
    filename = 'Who Moved My Cheese.txt'  # 英文文件名
    filename_cn = 'scientist.txt'  # 用于生成词云的中文文件名
    content = read_file(filename)  # 调用函数返回字典类型的数据
    frequency_result = word_frequency(content)
    draw_cloud_en_freq(frequency_result)
    draw_cloud_en_txt(content)
    content_cn = read_file_cn(filename_cn)
    frequency = word_frequency_cn(content_cn)  # 利用jieba对文本进行分词，并统计词频
    draw_cloud_cn(frequency)  # 绘制词云
