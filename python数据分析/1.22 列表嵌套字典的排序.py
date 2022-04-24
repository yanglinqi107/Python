N = int(input())
lst = []
for i in range(0, N):
    s = input()
    name, age = s.split()
    dic = {'name':name, 'age':int(age)}
    lst.append(dic)
    i += 1
print(sorted(lst, key = lambda x:x['age']))
print(sorted(lst, key = lambda x:x['name']))
