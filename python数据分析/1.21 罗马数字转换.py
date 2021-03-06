SYMBOL_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
s = input()
ans = 0
n = len(s)
for i, ch in enumerate(s):   # enumerate获取下标和元素
    value = SYMBOL_VALUES[ch]
    if i < n - 1 and value < SYMBOL_VALUES[s[i + 1]]:
        ans -= value
    else:
        ans += value
print(ans)