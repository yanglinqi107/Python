lst1 = [('dungeon', 7), ('winterfell', 4), ('bran', 9), ('meelo', 6)]
lst2 = [['Angle', '0121701100106', 99], ['Jack', '0121701100107', 86],
        ['Tom', '0121701100109', 65], ['Smith', '0121701100111', 100],
        ['Bob', '0121701100115', 77], ['Lily', '0121701100117', 59]]

m = int(input())
n = int(input())
print(sorted(lst1, key=lambda x: x[1])[:m])
print(sorted(lst2, key=lambda x: x[0])[:n])
print(sorted(lst2, key=lambda x: x[2])[:n])
