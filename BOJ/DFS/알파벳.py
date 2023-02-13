import sys
from collections import deque
input = sys.stdin.readline

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
board = []
for _ in range(R):
    line = input().strip()
    board_line = []
    for i in range(C):
        board_line.append(line[i])
    board.append(board_line)


def dfs(ci, cj, cw):
    max_res = cw
    for i in range(4):
        ni = ci + dr[i]
        nj = cj + dc[i]
        nw = cw + 1

        if ni == -1 or ni == R or nj == -1 or nj == C:
            continue

        if visited[ni][nj]:
            continue

        if alphas[ord(board[ni][nj])-65]:
            continue

        visited[ni][nj] = True
        alphas[ord(board[ni][nj])-65] = True
        max_res = max(max_res, dfs(ni, nj, nw))
        visited[ni][nj] = False
        alphas[ord(board[ni][nj]) - 65] = False

    return max_res


visited = [[False] * C for _ in range(R)]
alphas = [False] * 26
visited[0][0] = True
alphas[ord(board[0][0])-65] = True

res = dfs(0, 0, 1)
print(res)

'''
2 4
CAAB
ADCB
'''