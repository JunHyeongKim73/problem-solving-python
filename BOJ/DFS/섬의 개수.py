import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 북 북동 동 남동 남 남서 서 북서
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(r, c, visited):
    visited[r][c] = True
    for n in range(8):
        nr = r + dr[n]
        nc = c + dc[n]

        if nr == -1 or nr == h:
            continue
        if nc == -1 or nc == w:
            continue
        if maps[nr][nc] == 0:
            continue
        if visited[nr][nc]:
            continue

        dfs(nr, nc, visited)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    maps = list()
    for _ in range(h):
        maps.append(list(map(int, input().split())))

    visited = [[False for j in range(w)] for i in range(h)]

    sums = 0
    for r in range(h):
        for c in range(w):
            if maps[r][c] == 0:
                continue
            if visited[r][c]:
                continue
            dfs(r, c, visited)
            sums += 1

    print(sums)

'''
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
0 0
'''
