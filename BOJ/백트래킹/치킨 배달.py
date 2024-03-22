import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
maps = list()
for _ in range(N):
    maps.append(list(map(int, input().split())))


def get_dist(r, c):
    dist = list()
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                dist.append((i, j, abs(r - i) + abs(c - j)))

    return dist


homes = list()
chickens = list()
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            homes.append((i, j))
        if maps[i][j] == 2:
            chickens.append((i, j))

homes_to_chickens = list()
for i, j in homes:
    for r, c in chickens:
        homes_to_chickens.append(((i, j), (r, c), abs(r - i) + abs(c - j)))

min_sums = 1e9
for combination in combinations(chickens, M):
    sums = 0
    for i, j in homes:
        min_dist = 1e9
        for r, c in list(combination):
            min_dist = min(min_dist, abs(r - i) + abs(c - j))

        sums += min_dist

    min_sums = min(min_sums, sums)

print(min_sums)
