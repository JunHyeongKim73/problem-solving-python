import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

R, C, K = map(int, input().split())
maps = []
for _ in range(R):
    maps.append(input().strip())


# 남북서동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[False] * C for _ in range(R)]


def dfs(r, c, k):
    global res

    if k == K and r == 0 and c == C - 1:
        res += 1
        return

    if k >= K:
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        nk = k + 1

        if nr == -1 or nr == R or nc == -1 or nc == C:
            continue

        if visited[nr][nc]:
            continue

        if maps[nr][nc] == 'T':
            continue

        visited[nr][nc] = True
        dfs(nr, nc, nk)
        visited[nr][nc] = False

    return

res = 0
visited[R-1][0] = True
dfs(R-1, 0, 1)

print(res)

'''
3 4 10
....
.T..
....
'''