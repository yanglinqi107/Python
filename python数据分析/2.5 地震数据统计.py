import pandas as pd

df = pd.read_csv('quake.csv', encoding='utf-8', dtype={'震级(M)':'str'})


def func1():
    n = int(input())
    dftmp = df.sort_values(by='深度(千米)', ascending=True,
                           kind='stable').loc[:, ['参考位置', '深度(千米)']].head(n)
    print(f'从低到高前{n}名:')
    for v in dftmp.values:
        print(f'{v[0]}:{v[1]}千米')
    dftmp = df.sort_values(by='深度(千米)', ascending=False,
                           kind='stable').loc[:, ['参考位置', '深度(千米)']].head(n)
    print(f'\n从高到低前{n}名:')
    for v in dftmp.values:
        print(f'{v[0]}:{v[1]}千米')


def func2():
    n = int(input())
    dftmp = df.sort_values(by='震级(M)', ascending=False,
                           kind='stable').loc[:, ['参考位置', '震级(M)']].head(n)
    for v in dftmp.values:
        print(f'{v[0]}:{v[1]}级')


def func3(choice):
    dftmp = df.loc[(df['参考位置'].str.contains(choice)), ['参考位置', '震级(M)']]
    if dftmp.empty:
        print("无数据")
        return
    for v in dftmp.values:
        print(f'{v[0]}:{v[1]}')


if __name__ == '__main__':
    choice = input()
    if choice == '震源深度':
        func1()
    elif choice == '震级':
        func2()
    else:
        func3(choice)