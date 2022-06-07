from sys import stdin
N, M = map(int, stdin.readline().strip().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, stdin.readline().strip().split())))

arr = []
for _ in range(M):
    arr.append(list(map(int, stdin.readline().strip().split())))

graph_sum = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        graph_sum[i][j] = graph_sum[i-1][j] + graph_sum[i][j-1] - graph_sum[i-1][j-1] + graph[i-1][j-1]

for x1, y1, x2, y2 in arr:
    ans = graph_sum[x2][y2] - (graph_sum[x1-1][y2] + graph_sum[x2][y1-1]) + graph_sum[x1-1][y1-1]
    print(ans)