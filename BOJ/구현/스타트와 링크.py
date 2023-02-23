import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
S = []
for _ in range(N):
    S.append(list(map(int, input().split())))

mins = 1e9
C = [i for i in range(N)]
for c in combinations(C, int(N/2)):
    start = []
    link = []
    for j in C:
        if j in c:
            start.append(j)
        else:
            link.append(j)

    starts = 0
    links = 0

    for i in start:
        for j in start:
            if i == j:
                continue
            starts += S[i][j]

    for i in link:
        for j in link:
            if i == j:
                continue
            links += S[i][j]

    mins = min(mins, abs(starts - links))

print(mins)