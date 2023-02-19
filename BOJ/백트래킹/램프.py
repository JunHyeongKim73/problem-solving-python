import sys

input = sys.stdin.readline

N, M = map(int, input().split())

m = {}
table = []
for _ in range(N):
    s = input().strip()
    table.append(s)
    if s in m:
        m[s] += 1
    else:
        m[s] = 1

K = int(input())

res = 0
for i in range(N):
    count = 0
    for j in range(M):
        if table[i][j] == '0':
            count += 1

    if count > K or (K-count) % 2 != 0:
        continue

    res = max(res, m[table[i]])

print(res)