import sys
import heapq
input = sys.stdin.readline

INF = 1e9
N, M, X = map(int, input().split())

adj = [[] for _ in range(N+1)]
inverse_adj = [[] for _ in range(N+1)]
for i in range(M):
    s, e, t = map(int, input().split())
    adj[s].append((e, t))
    inverse_adj[e].append((s, t))


def solve(adj):
    q = []
    dist = [INF] * (N+1)
    heapq.heappush(q, (X, 0))
    while q:
        s, min_weight = heapq.heappop(q)
        if dist[s] < min_weight:
            continue

        for e, t in adj[s]:
            cost = min_weight + t
            if cost < dist[e]:
                dist[e] = cost
                heapq.heappush(q, (e, cost))

    return dist


res_adj = solve(adj)
res_inv = solve(inverse_adj)

res = [res_adj[i]+res_inv[i] for i in range(1, N+1) if i != X]
print(max(res))

'''
4 8 1
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''