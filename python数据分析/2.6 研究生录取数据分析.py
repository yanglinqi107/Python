import pandas as pd

df = pd.read_csv('admit2.csv', encoding='utf-8')
# print(df.columns)


def func1():
    dftmp = df.loc[(df['Chance of Admit '] >= 0.8), :]
    num1 = dftmp.shape[0]
    dftmp = dftmp.loc[(df['University Rating'] >= 4), :]
    num2 = dftmp.shape[0]
    print("Top University in >=80%:{:.2f}%".format(num2 * 100 / num1))


def func2():
    dftmp = df.loc[(df['Chance of Admit '] >= 0.9), :]
    num1 = dftmp.shape[0]
    dftmp = dftmp.loc[(df['Research'] == 1), :]
    num2 = dftmp.shape[0]
    print("Reseach in >=90%:{:.2f}%".format(num2 * 100 / num1))
    dftmp = df.loc[(df['Chance of Admit '] <= 0.7), :]
    num1 = dftmp.shape[0]
    dftmp = dftmp.loc[(df['Research'] == 1), :]
    num2 = dftmp.shape[0]
    print("Reseach in <=70%:{:.2f}%".format(num2 * 100 / num1))


def func3():
    dftmp = df.loc[(df['Chance of Admit '] >= 0.8), 'TOEFL Score']
    print("TOEFL Average Score:{:.2f}".format(dftmp.mean()))
    print("TOEFL Max Score:{:.2f}".format(dftmp.max()))
    print("TOEFL Min Score:{:.2f}".format(dftmp.min()))


def func4():
    dftmp = df.loc[(df['Chance of Admit '] >= 0.8), 'CGPA']
    print("CGPA Average Score:{:.3f}".format(dftmp.mean()))
    print("CGPA Max Score:{:.3f}".format(dftmp.max()))
    print("CGPA Min Score:{:.3f}".format(dftmp.min()))


if __name__ == '__main__':
    n = input()
    if n == '1':
        func1()
    elif n == 'Research':
        func2()
    elif n == '2':
        func3()
    elif n == '3':
        func4()
    else:
        print("ERROR")