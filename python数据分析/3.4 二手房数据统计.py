import pandas as pd

df = pd.read_csv("house.csv", encoding='GBK')
# df = df.astype({'面积(㎡)': 'int', '价格(万元)': 'int'})
# print(df.info())


def func1():
    k = int(input())
    dftmp = df.sort_values(by="价格(万元)", kind='stable', ascending=False).head(k)
    print("市区 小区 户型 朝向 楼层 装修情况 电梯 面积(㎡) 价格(万元) 年份")
    for index in dftmp.index:
        print("%s %s %s %s %d %s %s %d %d %d" %
              (dftmp.loc[index].values[0], dftmp.loc[index].values[1],
               dftmp.loc[index].values[2], dftmp.loc[index].values[3],
               dftmp.loc[index].values[4], dftmp.loc[index].values[5],
               dftmp.loc[index].values[6], dftmp.loc[index].values[7],
               dftmp.loc[index].values[8], dftmp.loc[index].values[9]))


def func2():
    k = int(input())
    dftmp = df.sort_values(by="面积(㎡)", ascending=False).head(k)
    print("市区 小区 户型 朝向 楼层 装修情况 电梯 面积(㎡) 价格(万元) 年份")
    for index in dftmp.index:
        print("%s %s %s %s %d %s %s %d %d %d" %
              (dftmp.loc[index].values[0], dftmp.loc[index].values[1],
               dftmp.loc[index].values[2], dftmp.loc[index].values[3],
               dftmp.loc[index].values[4], dftmp.loc[index].values[5],
               dftmp.loc[index].values[6], dftmp.loc[index].values[7],
               dftmp.loc[index].values[8], dftmp.loc[index].values[9]))


def func3():
    df['单价'] = df['价格(万元)'] / df['面积(㎡)']
    dftmp = df.sort_values(by="单价", ascending=False).head(1)
    print("市区 小区 户型 朝向 楼层 装修情况 电梯 面积(㎡) 价格(万元) 年份")
    for index in dftmp.index:
        print("%s %s %s %s %d %s %s %d %d %d" %
              (dftmp.loc[index].values[0], dftmp.loc[index].values[1],
               dftmp.loc[index].values[2], dftmp.loc[index].values[3],
               dftmp.loc[index].values[4], dftmp.loc[index].values[5],
               dftmp.loc[index].values[6], dftmp.loc[index].values[7],
               dftmp.loc[index].values[8], dftmp.loc[index].values[9]))


def func4():
    dftmp = df.loc[(df['装修情况'] == '精装') & (df['电梯'] == '有电梯'),
                   ['面积(㎡)', '价格(万元)']]
    avg = dftmp['价格(万元)'].sum() / dftmp['面积(㎡)'].sum()
    print("%.2f万元" % (avg))
    # for index in dftmp.index:
    #     print("%.2f万元" % (dftmp.loc[index, '单价']))


def func5():
    k = str(input())
    dftmp = df.loc[df['朝向'] == k, :]
    if dftmp.empty:
        print("无数据")
    else:
        print("%d套" % (len(dftmp)))


def func5():
    k = str(input())
    dftmp = df.loc[df['朝向'] == k, :]
    if dftmp.empty:
        print("无数据")
    else:
        print("%d套" % (len(dftmp)))


def func6(scanin):
    dftmp = df.loc[df['小区'].str.contains(scanin), :]
    print("市区 小区 户型 朝向 楼层 装修情况 电梯 面积(㎡) 价格(万元) 年份")
    if dftmp.empty:
        print('未找到相关数据')
        return
    for index in dftmp.index:
        print("%s %s %s %s %d %s %s %d %d %d" %
              (dftmp.loc[index].values[0], dftmp.loc[index].values[1],
               dftmp.loc[index].values[2], dftmp.loc[index].values[3],
               dftmp.loc[index].values[4], dftmp.loc[index].values[5],
               dftmp.loc[index].values[6], dftmp.loc[index].values[7],
               dftmp.loc[index].values[8], dftmp.loc[index].values[9]))


def main():
    scanin = input()
    if scanin == '最高总价':
        func1()
    elif scanin == '最大面积':
        func2()
    elif scanin == '最高单价':
        func3()
    elif scanin == '精装电梯房单价':
        func4()
    elif scanin == '房屋朝向':
        func5()
    else:
        func6(scanin)


if __name__ == "__main__":
    main()