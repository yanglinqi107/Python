# from decimal import Decimal
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import re


# 读取文件内容，用正则将10中语言的数据提取放入列表中
def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        s = f.read()
    lst = re.findall(r"{name.*?}", s, re.S)
    return lst


def data_to_dataframe(string):
    df = pd.DataFrame(columns=['日期', '占比'])
    result = re.finditer(r'\[Date.UTC\((?P<date>.*?)\), (?P<d>.*?)\]', string,
                         re.S)
    for i in result:
        y, m, d = i.group('date').split(',')
        m = int(m) + 1
        datestr = "{}-{}-{}".format(int(y), m, int(d))
        df.loc[df.shape[0]] = [datestr, i.group('d')]  # 日期 y-m-d字符串
    return df


def draw1(df_lst, name_lst):
    # 引入中文字体
    plt.rcParams['font.family'] = ['Microsoft YaHei']
    plt.rcParams.update({"font.size": 10})
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(1, 1, 1)
    i = 0
    for df in df_lst:
        x = pd.to_datetime(df['日期'])
        y = df['占比'].astype(float)
        if i == 0:
            ax.plot(x, y, linewidth=4, label=name_lst[i])
        else:
            ax.plot(x, y, linewidth=2, label=name_lst[i])
        i += 1
    ax.xaxis.set_major_locator(mdates.YearLocator(2))  # 设置x轴的间隔
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))  # 设置x轴日期格式
    # plt.axhline(y=5, linestyle='--')
    plt.grid(axis='y', linestyle='-.')
    plt.legend(loc='lower center', ncol=5, bbox_to_anchor=(0.5, -0.15))
    plt.title("The TIOBE Programming Community index")
    plt.ylabel('热度')
    # plt.legend()
    plt.show()


def draw2(name_lst, sizes):
    # sum = 0.00
    # for f in sizes:
    #     sum = Decimal(str(sum)) + Decimal(str(f))   # 为什么就是算不出来精确数值
    # print(round(sum, 1))
    name_lst.append('other')
    sizes.append('37.5')
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # 第1个数据突出显示
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(1, 1, 1)
    # plt.axes(aspect=1)  # 设置参数为1使饼图是圆的
    colors = [
        '#8000ff', '#5247fc', '#2489f5', '#0ac0e8', '#3ae8d6', '#69fcc1',
        '#96fca7', '#c4e88a', '#f4c069', '#ff8947', '#ff4724'
    ]
    patches, l_text, p_text = ax.pie(sizes,
                                     explode=explode,
                                     colors=colors,
                                     labels=name_lst,
                                     labeldistance=1.1,
                                     autopct='%2.1f%%',
                                     shadow=True,
                                     startangle=90,
                                     pctdistance=0.8)
    # 设置饼图百分比字体的大小
    for p in p_text:
        p.set_size(7)
    # 设置每个扇形标签的大小
    for l in l_text:
        l.set_size(10)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.16), ncol=3, fontsize=10)
    plt.show()


def main():
    file = "tiobe202112.txt"
    lst = read_file(file)
    name_lst = []
    for s in lst:
        name_lst += re.findall(r"{name : '(.*?)',", s, re.S)  # 编程语言的名称
    # 图1
    df_lst = []
    for s in lst:
        df_lst.append(data_to_dataframe(s))
    draw1(df_lst, name_lst)
    # 图2
    sizes = []
    for df in df_lst:
        sizes.append(df.loc[df.shape[0] - 1, '占比'])
    draw2(name_lst, sizes)


if __name__ == '__main__':
    main()