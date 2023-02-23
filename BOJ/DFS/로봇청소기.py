import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)
# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
R = []
r, c, d = map(int, input().split())
for _ in range(N):
    R.append(list(map(int, input().split())))


def possible(ci, cj):
    for i in range(4):
        ni = ci + dr[i]
        nj = cj + dc[i]
        if R[ni][nj] == 0:
            return True

    return False

nums = 0
def dfs(ci, cj, d):
    global nums
    if R[ci][cj] == 0:
        nums += 1
        R[ci][cj] = -1

    if possible(ci, cj):
        nd = (d-1) % 4
        ni = ci + dr[nd]
        nj = cj + dc[nd]

        if R[ni][nj] == 0:
            dfs(ni, nj, nd)
        else:
            dfs(ci, cj, nd)

    else:
        nd = (d - 2) % 4
        ni = ci + dr[nd]
        nj = cj + dc[nd]
        if R[ni][nj] == 1:
            return
        else:
            dfs(ni, nj, d)

dfs(r, c, d)
print(nums)

'''
4 4
1 1 0
1 1 1 1 
1 0 0 1
1 0 0 1
1 1 1 1
'''