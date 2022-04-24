import pandas as pd
import numpy as np

df = pd.read_csv("tips.csv")


def func1():
    stmp = df['tip'].groupby(df['gender']).mean()
    print("男性顾客平均小费为：%.2f" % (stmp['Male']))
    print("女性顾客平均小费为：%.2f" % (stmp['Female']))


def func2():
    stmp = df['tip'].groupby(df['day']).mean().sort_values()
    for index in stmp.index:
        print("%s：%.2f" % (index, stmp[index]))


def func3():
    tmp = df.groupby('time')[['total_bill', 'tip']]
    # print(type(tmp.sum()))
    # print(tmp.count())
    lc = tmp.count().loc['Lunch', 'total_bill']
    ls = tmp.sum().loc['Lunch', 'total_bill']
    lv = ls / lc
    lvt = tmp.mean().loc['Lunch', 'tip']
    dc = tmp.count().loc['Dinner', 'total_bill']
    ds = tmp.sum().loc['Dinner', 'total_bill']
    dv = ds / dc
    dvt = tmp.mean().loc['Dinner', 'tip']
    print("午餐时间共%d条记录，共消费%.2f，平均每单消费%.2f，平均小费%.2f" % (lc, ls, lv, lvt))
    print("晚餐时间共%d条记录，共消费%.2f，平均每单消费%.2f，平均小费%.2f" % (dc, ds, dv, dvt))


def func4():
    n = input()
    dftmp = df.loc[(df['gender'] == n) & (df['smoker'] == "Yes") &
                   (df['total_bill'] > 30)]
    for index in dftmp.index:
        print(list(dftmp.loc[index].values))


def func5():
    n = int(input())
    df['人均消费'] = df['total_bill'] / df['size']
    dftmp = df.sort_values(by='人均消费', kind='stable', ascending=False).head(n)
    for index in dftmp.index:
        print(list(df.loc[index].values[:7]))


def main():
    scanin = input()
    if scanin == 'gender':
        func1()
    elif scanin == 'day':
        func2()
    elif scanin == 'time':
        func3()
    elif scanin == 'smoker':
        func4()
    elif scanin == 'average':
        func5()
    else:
        print("无数据")


if __name__ == "__main__":
    main()