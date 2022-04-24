import pandas as pd

df = pd.read_csv('2012-19sport.csv', encoding='utf-8')


def func1(year):
    if year not in range(2012, 2020):
        print('Wrong Input')
    else:
        k = int(input())
        dftmp = df.loc[(df['Year'] == year), :].head(k)
        for v in dftmp.values:
            print("{} | {} | {} | {} | {} | {} | {}".format(v[0].strip('#'), v[1], v[2], v[3], v[4], v[5], v[6]))


def func2():
    year = int(input())
    if year not in range(2012, 2020):
        print('Wrong Input')
    else:
        dftmp = df.loc[(df['Year'] == year), :]
        lst = sorted(set(dftmp['Sport']))
        for i, v in enumerate(lst):
            print(f'{i+1}: {v}')
        k = int(input())
        dftmp = dftmp.loc[(df['Sport'] == lst[k-1]), :]
        for v in dftmp.values:
            print("{} | {} | {} | {} | {} | {} | {}".format(v[0].strip('#'), v[1], v[2], v[3], v[4], v[5], v[6]))
        sum = dftmp['Pay'].str[1:-1].astype(float).sum()
        print('TOTAL: ${:.2f} M'.format(sum))

if __name__ == '__main__':
    s = input()
    if s.isdigit():
        func1(int(s))
    elif s.lower() == 'sport':
        func2()
    else:
        print('Wrong Input')
