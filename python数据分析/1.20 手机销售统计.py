choice = input()
data1 = set()
with open('sale2018.csv', 'r', encoding='utf-8') as f:
    for line in f:
        data1.add(line.strip().split(',')[0])
data2 = set()
with open('sale2019.csv', 'r', encoding='utf-8') as f:
    for line in f:
        data2.add(line.strip().split(',')[0])
if choice == '1':
    print(sorted(data2))
    print(sorted(data1))
elif choice == '2':
    print(sorted(data1 & data2))  # 交集
elif choice == '3':
    print(sorted(data1 | data2))  # 并集
elif choice == '4':
    print(sorted(data2 - data1))  # 差集data2有而data1没有
elif choice == '5':
    print(sorted(data1 ^ data2))  # 补集