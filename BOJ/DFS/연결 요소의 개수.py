import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

visited = [False for _ in range(N+1)]
adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def dfs(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v)


nums = 0
for u in range(1, N+1):
    if not visited[u]:
        nums += 1
        dfs(u)

print(nums)
