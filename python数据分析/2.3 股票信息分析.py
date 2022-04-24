import pandas as pd

df = pd.read_csv('China Minsheng Bank.csv',
                 encoding='utf-8',
                 dtype={
                     '收盘价': 'str',
                     '最高价': 'str',
                     '最低价': 'str',
                     '开盘价': 'str'
                 })


def func1():
    n = int(input())
    dftmp = df.sort_values(by='最高价', kind='stable',
                           ascending=False).loc[:, ['日期', '最高价']].head(n)
    print(f"最高价从高到低前{n}名:")
    for v in dftmp.values:
        print('{0} {1}元'.format(v[0], v[1]))


def func2():
    n = int(input())
    dftmp = df.sort_values(by='开盘价', kind='stable').loc[:, ['日期', '开盘价']].head(n)
    print(f"开盘价从低到高前{n}名:")
    for v in dftmp.values:
        print('{0} {1}元'.format(v[0], v[1]))


def func3():
    num = int(input())
    dftmp = df.sort_values(by='成交金额', kind='stable',
                           ascending=False).loc[:, '成交金额'].head(num)
    print('成交金额最多的{}天成交额为{}元'.format(num, dftmp.sum()))


def func4():
    date = input()
    dftmp = df.loc[(df['日期'] == date)]
    for v in dftmp.values:
        print('{} {} {} {} {} {} {} {}'.format(v[0], v[1], v[2], v[3], v[4],
                                               v[5], v[6], v[7]))


def main():
    choice = input()
    if choice == '最高价':
        func1()
    elif choice == '开盘价':
        func2()
    elif choice == '成交金额':
        func3()
    elif choice == '日期':
        func4()


if __name__ == '__main__':
    main()