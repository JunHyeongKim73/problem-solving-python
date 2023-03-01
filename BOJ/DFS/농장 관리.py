import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

# S N W E SW SE NW NE
dr = [1, -1, 0, 0, 1, 1, -1, -1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

visited = [[False] * M for _ in range(N)]


def dfs(r, c):
    global flag
    visited[r][c] = True
    h = maps[r][c]

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr == -1 or nr == N or nc == -1 or nc == M:
            continue

        if maps[nr][nc] > h:
            flag = False

        if not visited[nr][nc] and maps[nr][nc] == h:
            dfs(nr, nc)


res = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        flag = True
        dfs(i, j)

        if flag:
            res += 1

print(res)


'''
8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0

3 3
2 1 2
1 0 1
2 1 2

3 3
0 1 2
1 2 3
2 3 4
'''