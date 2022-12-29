import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, s, w = map(int, input().split())
    
    adj[p].append((s, w))
    adj[s].append((p, w))

visited = [False for _ in range(n+1)]
def solve(start):
    
    visited[start] = True

    max_cost = -1
    max_node = -1
    count = 0
    for n_n, w in adj[start]:
        if visited[n_n]:
            continue

        node, cost = solve(n_n)
        cost += w

        if max_cost < cost:
            max_cost = cost
            max_node = node
        
        count += 1
    
    if count == 0:
        return start, 0

    return max_node, max_cost


if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    node, cost = solve(1)
    visited = [False for _ in range(n+1)]

    n_node, res = solve(node)
    print(res)

'''
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
'''