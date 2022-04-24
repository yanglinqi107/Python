# ------------      -------    --------    -----------    -----------
# @File       : 10.4.1A 绘制X 射线衍射曲线实验模板.py
# @Contact    : vasp@qq.com
# @Copyright  : 2018-2025, Wuhan University of Technology
# @Modify Time: 2021/4/27 22:40
# @Author     : 赵广辉
# @Version    : 1.0
# @License    : 仅限用于Python程序设计基础实践教程(赵广辉,高等教育出版社)配套实验
# ------------      -------    --------    -----------    -----------

import matplotlib.pyplot as plt


def read_file(filename):
    """
    @参数 filename：带路径的文件名，字符串
    接收文件名为参数，读取文件中的数据转为值是浮点数的二维列表，原文件的两列数据分别作为横、纵坐标数据。
    返回列表。
    """
    # =======================================================
    ret = []
    x = []
    y = []
    with open(filename, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f:
            coord_xy = line.strip().split('\t')
            x.append(float(coord_xy[0]))
            y.append(float(coord_xy[1]))
    ret.append(x)
    ret.append(y)
    return ret

    # =======================================================


def plot_xrd_a(data_list):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    接收一个列表为参数，列表的元素为包含x和y数据的列表
    绘制问题1的曲线。
    """
    # =======================================================
    plt.plot(data_list[0], data_list[1])
    plt.show()
    # =======================================================


def plot_xrd_b(data_list):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    接收一个列表为参数，列表的元素为包含x和y数据的列表。
    绘制问题2的曲线。
    """
    # =======================================================
    plt.rc('font', family='SimHei')  # 设置中文显示、字体大小
    plt.plot(data_list[0], data_list[1], color="red")
    plt.title("X射线衍射图谱")
    plt.ylabel("Intensity")
    plt.xlabel("2d")
    plt.axhline(color='blue', linestyle='--')
    plt.axvline(color='red', linestyle='--')
    plt.show()

    # =======================================================


def top_five_peak(data_list):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    接收数据列表为参数，返回纵坐标值最大的5个峰的坐标的列表，降序排序。
    """
    # =======================================================
    ret = []
    x = data_list[0]
    y = data_list[1]
    for index in range(1, len(y) - 1):
        if (y[index] > y[index - 1]) & (y[index] > y[index + 1]):
            ret.append([x[index], y[index]])
    ret.sort(key=lambda a: a[1], reverse=True)
    # print(ret[:5])
    return ret[:5]

    # =======================================================


def mark_peak(sort_of_ls):
    """
    @参数 sort_of_ls：排序后的数据列表，列表类型
    接收排序的数据，在指定的坐标点加注释。注释标记点相对横坐标偏移+30，纵坐标等高，
    注释文本为峰高，即y 值。
    """
    # =======================================================
    for i in sort_of_ls:
        i[0] += 30.0
        i[0] = round(i[0], 2)
    return sort_of_ls

    # =======================================================


def plot_xrd_c(data_list, sort_of_ls):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    @参数 sort_of_ls：排序后的数据列表，列表类型
    接收一个元组为参数，元组的元素为包含x和y数据的列表
    绘制问题3的曲线。
    """
    # =======================================================
    # sort_of_ls = mark_peak(sort_of_ls)
    # print(sort_of_ls)
    plt.rc('font', family='SimHei')  # 设置中文显示、字体大小
    plt.plot(data_list[0], data_list[1], color="red")
    plt.title("X射线衍射图谱")
    plt.ylabel("Intensity")
    plt.xlabel("2d")
    plt.axhline(color='blue', linestyle='--')
    plt.axvline(color='red', linestyle='--')
    for i in sort_of_ls:
        plt.annotate(text=str(i[1]),
                     xy=(i[0], i[1]),
                     xytext=(i[0] + 3, i[1]),
                     arrowprops=dict(arrowstyle="->",
                                     connectionstyle="arc3,rad=.2"))
    plt.show()

    # =======================================================


def plot_xrd_d(data_list, sort_of_ls):
    """
    @参数 data_list：读文件获得的数据列表，列表类型
    @参数 sort_of_ls：排序后的数据列表，列表类型
    接收一个元组为参数，元组的元素为包含x和y数据的列表
    绘制问题4的曲线。
    """
    # =======================================================
    plt.subplot(2, 1, 1)
    plt.rc('font', family='SimHei')  # 设置中文显示、字体大小
    plt.plot(data_list[0], data_list[1], color="red")
    plt.title("X射线衍射图谱")
    plt.ylabel("Intensity")
    plt.xlabel("2d")
    plt.axhline(color='blue', linestyle='--')
    plt.axvline(color='red', linestyle='--')
    for i in sort_of_ls:
        plt.annotate(text=str(i[1]),
                     xy=(i[0], i[1]),
                     xytext=(i[0] + 3, i[1]),
                     arrowprops=dict(arrowstyle="->",
                                     connectionstyle="arc3,rad=.2"))

    plt.subplot(2, 2, 3)
    plt.plot(data_list[0], data_list[1])
    plt.xlim(6.7, 7.0)

    plt.subplot(2, 2, 4)
    plt.plot(data_list[0], data_list[1])
    plt.xlim(9.5, 10.0)
    plt.show()

    # =======================================================


if __name__ == '__main__':
    file = 'XRD_AFO.txt'  # 带路径文件名
    file_to_list = read_file(file)
    plot_xrd_a(file_to_list)
    plot_xrd_b(file_to_list)
    top_peak = top_five_peak(file_to_list)
    plot_xrd_c(file_to_list, top_peak)
    plot_xrd_d(file_to_list, top_peak)
