import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input().strip())

cache = [[0]*(m+1) for _ in range(n+1)]
res = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i-1][j-1] == '0':
            continue

        cache[i][j] = min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1]) + 1
        res = max(res, cache[i][j])

print(res**2)