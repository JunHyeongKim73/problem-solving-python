import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

cache = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N-i):
        s, e = j, j+i
        if nums[s] != nums[e]:
            cache[s][e] = False
            continue

        if e - s <= 2:
            cache[s][e] = True
        elif cache[s+1][e-1]:
            cache[s][e] = True
        else:
            cache[s][e] = False

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    if cache[S-1][E-1]:
        print(1)
    else:
        print(0)