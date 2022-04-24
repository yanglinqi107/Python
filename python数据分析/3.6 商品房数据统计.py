import pandas as pd

df = pd.read_csv("wuhan2021s1.csv",
                 encoding='GBK',
                 dtype={'可售住宅总规模（㎡）': 'str'})
# print(df)


def func1():
    dftmp = df.sort_values(by='可售住宅总规模（㎡）',
                           kind='stable',
                           key=lambda x: x.astype(float))
    for index in dftmp.index:
        print("%d %s %s %s %s %s" %
              (dftmp.loc[index][0], dftmp.loc[index][1], dftmp.loc[index][2],
               dftmp.loc[index][3], dftmp.loc[index][4],
               str(dftmp.loc[index][5])))


def func2():
    dftmp = df.sort_values(by='可售住宅总规模（㎡）',
                           kind='stable',
                           ascending=False,
                           key=lambda x: x.astype(float))
    for index in dftmp.index:
        print("%d %s %s %s %s %s" %
              (dftmp.loc[index][0], dftmp.loc[index][1], dftmp.loc[index][2],
               dftmp.loc[index][3], dftmp.loc[index][4],
               str(dftmp.loc[index][5])))


def func3():
    sum = df['可售住宅总规模（㎡）'].astype(float).sum()
    print("%.2f平方米" % (sum))


def func4(scanin):
    dftmp = df.loc[df['区属'] == scanin, :]
    if dftmp.empty:
        print("错误输入")
        return
    for index in dftmp.index:
        print("%d %s %s %s %s %s" %
              (dftmp.loc[index][0], dftmp.loc[index][1], dftmp.loc[index][2],
               dftmp.loc[index][3], dftmp.loc[index][4],
               str(dftmp.loc[index][5])))
    sum = dftmp['可售住宅总规模（㎡）'].astype(float).sum()
    print("%.2f平方米" % (sum))


def main():
    scanin = input()
    if scanin == '规模升序':
        func1()
    elif scanin == '规模降序':
        func2()
    elif scanin == '总规模':
        func3()
    else:
        func4(scanin)


if __name__ == "__main__":
    main()