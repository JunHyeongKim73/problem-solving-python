import sys
input = sys.stdin.readline

INF = 1e9

TC = int(input())

def bellman_ford(adj, dist, N, start):
    dist[start] = 0
    
    # N번 반복
    # N-1번만 반복하면 되지만 N번째에 음수 간선 순환 여부를 파악할 수 있다
    for i in range(N):
        # (M + W)번 반복
        for c_n in range(1, N+1):
            for n_n, cost in adj[c_n]:
                # 현재 간선을 거쳐서 가는게 더 짧은 경우
                if dist[n_n] > dist[c_n] + cost:
                    dist[n_n] = dist[c_n] + cost

                    if i == N-1:
                        return True
                    
    return False


while TC:
    N, M, W = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    dist = [INF for _ in range(N+1)]
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        adj[S].append((E, T))
        adj[E].append((S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        adj[S].append((E, -T))

    is_possible = bellman_ford(adj, dist, N, 0)
    
    if is_possible:
        print("YES")
    else:
        print("NO")

    TC -= 1


'''
2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8
'''