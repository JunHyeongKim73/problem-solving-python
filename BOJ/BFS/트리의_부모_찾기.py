from sys import stdin
from collections import deque

N = int(input())
adj = [[] for _ in range(N + 1)]

for _ in range(N - 1):
	a, b = map(int, stdin.readline().split())
	adj[a].append(b)
	adj[b].append(a)

parent = [-1] * (N + 1)
q = deque()

start = 1
q.append(start)

while q:
	s = q.pop()
	for e in adj[s]:
		if parent[e] != -1:
			continue
		parent[e] = s
		q.append(e)

print(*parent[2:])