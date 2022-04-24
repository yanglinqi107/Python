import pandas as pd

df = pd.read_csv("2019Charity.csv")
# print(df.columns)


def Total_func():
    sum = df['现金捐赠总额（万元）'].sum()
    print("Total:%d万元" % (sum))


def digit_func(scanin):
    if scanin not in range(101):
        print("No Record")
        return
    dftmp = df.loc[df['排名'] == scanin, :]
    for indexs in dftmp.index:
        st = df.loc[indexs].values
        print("{0} {1} {2} {3} {4} {5}".format(st[0], st[1], st[2], st[3],
                                               st[4], st[5]))


def loc_func(scanin):
    dftmp = df.loc[df['总部（省份）'] == scanin, ['排名', '姓名', '企业简称', '总部（省份）']]
    if dftmp.empty:
        print("No Record")
        return
    for indexs in dftmp.index:
        st = df.loc[indexs].values
        print("{0} {1} {2} {3}".format(
            st[0],
            st[1],
            st[2],
            st[3],
        ))


def main():
    # print(df)
    scanin = input()
    if scanin.isdigit():
        scanin = int(scanin)
        digit_func(scanin)
    elif scanin.lower() == 'total':
        Total_func()
    else:
        loc_func(scanin)


if __name__ == "__main__":
    main()