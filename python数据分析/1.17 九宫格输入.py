keyboard = [['0', ' '], ['1', ',', '.', '?', '!'], ['2', 'A', 'B', 'C'],
            ['3', 'D', 'E', 'F'], ['4', 'G', 'H', 'I'], ['5', 'J', 'K', 'L'],
            ['6', 'M', 'N', 'O'], ['7', 'P', 'Q', 'R', 'S'],
            ['8', 'T', 'U', 'V'], ['9', 'W', 'X', 'Y', 'Z']]
instr = input()
lst = instr.split()
result = ""
for s in lst:
    num = int(s[0])
    times = len(s)
    size = len(keyboard[num])
    n = times % size - 1
    result += keyboard[num][n]
print(result)