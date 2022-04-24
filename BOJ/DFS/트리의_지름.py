from sys import stdin
V = int(stdin.readline())
l = [[] for _ in range(V)]
adj = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

def Solve(i, s):
	if len(adj[i]) == 1 and i != s:
		return 0, i

	maxs = -1
	max_v = -1
	for next, w in adj[i]:
		if visited[next]:
			continue

		visited[next] = True
		length, v = Solve(next, s)
		if maxs < length + w:
			maxs = length + w
			max_v = v
		
	return maxs, max_v

for i in range(V):
	l[i] = list(map(int, stdin.readline().strip().split()))

for i in range(V):
	list_len = len(l[i])
	v = l[i][0]
	for j in range(1, list_len, 2):
		if l[i][j] == -1:
			break
		adj[v].append((l[i][j], l[i][j+1]))

visited[1] = True
res, v = Solve(1, 1)

visited = [False for _ in range(V+1)]
visited[v] = True
res, v = Solve(v, v)

print(res)
