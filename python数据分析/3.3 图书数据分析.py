import pandas as pd

df = pd.read_csv("CBOOK.csv", encoding='GBK')
# print(df.info())
# exit(0)

def rank_func():
    num = int(input())
    dftmp = df.loc[df['编号'] == num]
    dftmp = dftmp.astype({'原价':'int'})
    for index in dftmp.index:
        for v in dftmp.loc[index].values:
            print(v)


def maxcomment_func():
    df['评论'] = df["评论数"].str.strip("条评论").astype(int)
    dftmp = df.sort_values(by="评论", ascending=False).head(10).loc[:, ['书名', '评论数']]
    for index in dftmp.index:
        print("%s %s"%(dftmp.loc[index].values[0], dftmp.loc[index].values[1]))


def maxname_func():
    n = int(input())
    sort_index = df.书名.str.len().sort_values(kind='stable', ascending=False).index
    dftmp = df.reindex(sort_index).head(n).loc[:, ['书名']]
    for index in dftmp.index:
        print(dftmp.loc[index].values[0])


def main():
    scanin = input()
    if scanin == 'record':
        print(df.shape[0] + 1)
    elif scanin == 'rank':
        rank_func()
    elif scanin == 'maxcomment':
        maxcomment_func()
    elif scanin == 'maxname':
        maxname_func()
    else:
        print("无数据")


if __name__ == "__main__":
    main()