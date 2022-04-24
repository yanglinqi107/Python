freqDict = eval(input())
# print(freqDict)
lst = input().split()
for word in lst:
    if word in freqDict.keys():
        freqDict[word] += 1
    else:
        freqDict[word] = 1
print(freqDict)
