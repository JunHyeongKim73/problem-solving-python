import sys
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]

starts = []
for i in range(N):
    l = list(map(int, input().split()))
    w = l[0]
    if l[1] == 0:
        starts.append((i+1, w))
    s = l[2:]
    for node in s:
        adj[node].append((i+1, w))


cache = [-1] * (N+1)


def dfs(n):
    if cache[n] != -1:
        return cache[n]

    maxs = 0
    for n_n, w in adj[n]:
        maxs = max(maxs, dfs(n_n) + w)

    cache[n] = maxs
    return cache[n]


res = -1
for s, w in starts:
    res = max(res, dfs(s)+w)

print(res)

'''
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6

5
5 0
1 1 1 
2 2 2
4 0
10 1 4
'''