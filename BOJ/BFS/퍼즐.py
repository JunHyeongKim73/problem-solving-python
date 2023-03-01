import sys
from collections import deque
input = sys.stdin.readline

# 남북서동
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def check(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] != (i * 3 + j + 1) % 9:
                return False

    return True

def to_str(board):
    s = ""
    for i in range(3):
        for j in range(3):
            s += str(board[i][j])

    return s

boards = []
for _ in range(3):
    boards.append(list(map(int, input().split())))

r, c = -1, -1
for i in range(3):
    for j in range(3):
        if boards[i][j] == 0:
            r, c = i, j
            break

q = deque()
q.append((boards, r, c, 0))

cache = dict()
strs = to_str(boards)
cache[strs] = True

res = -1
while q:
    board, r, c, w = q.popleft()

    if check(board):
        res = w
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr == -1 or nr == 3 or nc == -1 or nc == 3:
            continue

        new_board = [[board[i][j] for j in range(3)] for i in range(3)]
        new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]

        strs = to_str(new_board)
        if strs in cache:
            continue

        cache[strs] = True
        q.append((new_board, nr, nc, w + 1))

print(res)