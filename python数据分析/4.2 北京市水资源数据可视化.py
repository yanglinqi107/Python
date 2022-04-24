import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 引入中文字体
plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams.update({"font.size":6})
plt.figure(dpi=128, figsize=(8, 8))

# 读取文件数据，文件编码为’GBK‘；
df = pd.read_csv('2001-2017年北京市水资源情况信息.csv', encoding='gbk')

# 数据预处理，再生水和南水北调水数据存在缺失值，请填充缺失值为0；
df = df.fillna(0)

# 添加子图1，绘制全年水资源量折线图；
#       x轴刻度为年份，隔2年显示，45度斜显示
#       y轴刻度为0至40,相隔5
plt.subplot(2, 2, 1)

year = list(df.columns[1:])
y1 = list(df.loc[0][1:])
y1_2 = list(df.loc[1][1:])
y1_3 = list(df.loc[2][1:])

plt.title('全年水资源量折线图', fontsize=8)
plt.xlabel('年份')
plt.ylabel('亿立方米')

plt.plot(year, y1, 'r', label='全年水资源总量')
plt.plot(year, y1_2, 'g', linestyle='--', label='全年地表水资源量')
plt.plot(year, y1_3, 'b', linestyle='dotted', label='全年地下水资源量')

plt.xticks(year[::2], rotation=45)
plt.yticks(np.arange(0, 41, 5))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
plt.legend(loc='upper left')

# 添加子图2，绘制人均水资源量散点图
#       绘制点的类型为circle('o'),颜色为蓝色
#       x轴刻度为年份，隔2年显示，45度斜显示
#       y轴刻度为100至200,相隔10
plt.subplot(2, 2, 2)

y2 = list(df.loc[3][1:])

plt.title('人均水资源量散点图', fontsize=8)
plt.xlabel('年份')
plt.ylabel('立方米/人')

plt.scatter(year, y2, label='人均水资源(立方米/人)')

plt.xticks(year[::2], rotation=45)
plt.yticks(np.arange(100, 205, step=10))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.25)
plt.legend(loc='upper right')

# 添加子图3，2017年用水饼图(农业用水、工业用水、生活用水、生态环境用水)
#       设置饼图中各个饼之间的间距均为01，百分比显示格式为小数点后保留2位；
plt.subplot(2, 2, 3)

tmp = list(df.loc[10:13]['2017'])
sum_water = sum(tmp)

plt.title('2017年用水量饼图', fontsize=8)

plt.pie(x=[i / sum_water * 100 for i in tmp],
        labels=[i.strip() for i in list(df.loc[10:13]['项    目'])],
        explode=[0.01 for i in range(len(tmp))],
        autopct='%.2f%%'
        )

# 添加子图4，2001-2017年万元地区生产总值耗水量柱状图
#       柱状图各参数使用默认值；
#       x轴刻度为年份，90度斜显示；
#       y轴刻度为10至110,相隔20；
#       使用plt.text方法在柱子上方添加具体数值显示，字体大小设置为7
plt.subplot(2, 2, 4)

y3 = list(df.loc[14][1:])

plt.title('2001-2017年万元地区生产总值耗水量柱状图', fontsize=8)

bar = plt.bar(year, y3)

plt.xticks(year[::1], rotation=90)
plt.yticks(np.arange(10, 111, 20))
plt.bar_label(bar, label_type='edge', fontsize=4.5)

# 保存文件名为result.png，并通过附件上传
plt.savefig('result.png')
