import sys

input = sys.stdin.readline

N, M = map(int, input().split())

parents = [i for i in range(N + 1)]


def find(n):
    if parents[n] == n:
        return n

    parents[n] = find(parents[n])
    return parents[n]


def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a < p_b:
        parents[p_b] = p_a
    else:
        parents[p_a] = p_b


for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

s = set()
for i in range(1, N+1):
    s.add(find(i))

print(len(s))
