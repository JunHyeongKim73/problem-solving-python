import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = []
for _ in range(M):
    A, B, C = map(int, input().split())
    adj.append((-C, A, B))

t1, t2 = map(int, input().split())

adj.sort()


def find(i):
    if par[i] == i:
        return par[i]
    par[i] = find(par[i])
    return par[i]


def union(a, b):
    p1, p2 = find(a), find(b)
    par[max(p1, p2)] = min(p1, p2)


par = [i for i in range(N+1)]
for c, a, b in adj:
    union(a, b)
    c = abs(c)

    if find(t1) == find(t2):
        print(c)
        break
