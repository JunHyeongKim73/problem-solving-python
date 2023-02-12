import sys
from collections import deque
input = sys.stdin.readline

# 위 아래 왼쪽 오른쪽 앞 뒤
dr = [0, 0, 0, 0, 1, -1]
dc = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

M, N, H = map(int, input().split())
box = []
for _ in range(H):
    one_box = []
    for _ in range(N):
        one_box.append(list(map(int, input().split())))
    box.append(one_box)


def bfs():
    q = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if box[k][i][j] == 1:
                    q.append((k, i, j, 0))

    max_w = 0
    while q:
        ck, ci, cj, cw = q.popleft()
        for i in range(6):
            ni = ci + dr[i]
            nj = cj + dc[i]
            nk = ck + dz[i]
            nw = cw + 1
            if ni == -1 or ni == N or nj == -1 or nj == M or nk == -1 or nk == H:
                continue

            if box[nk][ni][nj] == 1 or box[nk][ni][nj] == -1:
                continue

            box[nk][ni][nj] = 1
            q.append((nk, ni, nj, nw))
            max_w = max(max_w, nw)

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if box[k][i][j] == 0:
                    return -1

    return max_w

res = bfs()
print(res)

'''
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0

5 3 3
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''