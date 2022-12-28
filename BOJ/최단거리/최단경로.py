from sys import stdin
from queue import PriorityQueue

V, E = map(int, stdin.readline().strip().split())
K = int(stdin.readline())

adj = [[] for _ in range(V+1)] 

for _ in range(E):
    u, v, w = map(int, stdin.readline().strip().split())
    adj[u].append((v, w))

INF = 20000000
res = [INF for _ in range(V+1)]
visited = [False for _ in range(V+1)]

# 다익스트라 알고리즘
def solve(start):
    res[start] = 0
    pq = PriorityQueue()
    pq.put((0, start))
    
    while not pq.empty():
        # 가장 작은 dist를 가진 노드를 찾는다
        _, v = pq.get()
        if visited[v]:
            continue

        visited[v] = True

        # 노드의 간선으로 다른 노드까지의 dist를 업데이트 한다
        for nv, nw in adj[v]:
            res[nv] = min(res[nv], res[v] + nw)
            pq.put((res[nv], nv))

if __name__ == "__main__":
    solve(K)
    for i in range(1, V+1):
        if res[i] == INF:
            print('INF')
        else:
            print(res[i])

'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

5 6
1
5 1 1
1 2 3
1 3 5
2 3 1
2 4 5
3 4 1
'''