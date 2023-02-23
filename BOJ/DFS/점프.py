import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

cache = [[-1] * N for _ in range(N)]

# 오른쪽/아래
dr = [0, 1]
dc = [1, 0]


def dfs(r, c):
    if r == N - 1 and c == N - 1:
        return 1

    if cache[r][c] != -1:
        return cache[r][c]

    sums = 0
    jump = arr[r][c]
    for i in range(2):
        if jump == 0:
            continue

        nr = r + jump * dr[i]
        nc = c + jump * dc[i]
        if nr <= -1 or nr >= N or nc <= -1 or nc >= N:
            continue

        sums += dfs(nr, nc)

    cache[r][c] = sums
    return cache[r][c]


res = dfs(0, 0)
print(res)

'''
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
'''