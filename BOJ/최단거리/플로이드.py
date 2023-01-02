import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 1e9
dist = [[INF for j in range(n+1)] for i in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

def solve():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cost = dist[k][j]

                dist[i][j] = min(dist[i][j], dist[i][k] + cost)        

solve()
for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j] == INF:
            print(0, end=' ')
        
        else:
            print(dist[i][j], end=' ')
    print()

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
'''