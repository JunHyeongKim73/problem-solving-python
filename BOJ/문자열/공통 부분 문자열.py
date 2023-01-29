import sys
input = sys.stdin.readline

s = input()
t = input()

if len(s) < len(t):
    s, t = t, s

max_num = 0
cache = [[0 for _ in range(4001)] for _ in range(4001)]
for i in range(len(t)):
    for j in range(len(s)):
        if t[i] == s[j]:
            cache[i+1][j+1] = cache[i][j] + 1
            max_num = max(max_num, cache[i+1][j+1])

print(max_num)
