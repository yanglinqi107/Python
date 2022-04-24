lst = []
n = int(input())
while n > 0:
    s = input()
    tmp = s.split()
    if tmp[0] == 'insert':
        lst.insert(int(tmp[1]), int(tmp[2]))
    elif tmp[0] == 'print':
        print(lst)
    elif tmp[0] == 'remove':
        lst.remove(int(tmp[1]))
    elif tmp[0] == 'append':
        lst.append(int(tmp[1]))
    elif tmp[0] == 'sort':
        lst.sort()
    elif tmp[0] == 'reverse':
        lst.reverse()
    elif tmp[0] == 'pop':
        lst.pop()
    n -= 1
