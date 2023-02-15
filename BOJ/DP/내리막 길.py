import sys
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

M, N = map(int, input().split())
maps = []
cache = [[-1 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
for _ in range(M):
    maps.append(list(map(int, input().split())))


def dfs(ci, cj):
    if cache[ci][cj] != -1:
        return cache[ci][cj]

    if ci == M - 1 and cj == N - 1:
        return 1

    nums = 0
    for i in range(4):
        ni = ci + dr[i]
        nj = cj + dc[i]

        if ni == -1 or ni == M or nj == -1 or nj == N:
            continue

        if visited[ni][nj]:
            continue

        if maps[ci][cj] <= maps[ni][nj]:
            continue

        visited[ni][nj] = True
        nums += dfs(ni, nj)
        visited[ni][nj] = False

    cache[ci][cj] = nums
    return nums


res = dfs(0, 0)
print(res)

'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

2 2
9 8
8 7

3 3
40 20 25
25 17 28
22 15 10
'''