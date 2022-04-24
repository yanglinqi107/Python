n = int(input())
locations = input().split()
# print(locations)
MySet = set(locations)
for i in range(0, n):
    lst = input().split()
    if lst[0] == 'add':
        MySet.add(lst[1])
    elif lst[0] == 'print':
        print(sorted(MySet))
    elif lst[0] == 'del':
        if lst[1] in MySet:
            MySet.discard(lst[1])
    elif lst[0] == 'clear':
        MySet.clear()
    elif lst[0] == 'update':
        MySet = (MySet | set(lst[1:]))
    i += 1
