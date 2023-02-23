import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
M = int(input())

arr = [[0] * N for _ in range(N)]

# 남동북서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c, n, d):
    arr[r][c] = n
    if n == 1:
        return

    nr = r + dr[d]
    nc = c + dc[d]

    if nr == -1 or nr == N or nc == -1 or nc == N:
        dfs(r, c, n, (d+1) % 4)
    elif arr[nr][nc] != 0:
        dfs(r, c, n, (d+1) % 4)
    else:
        dfs(nr, nc, n-1, d)


dfs(0, 0, N**2, 0)
for i in range(N):
    for j in range(N):
        if arr[i][j] == M:
            res_i, res_j = i, j
        print(arr[i][j], end=' ')
    print()
print(res_i+1, res_j+1)