import sys
import heapq

input = sys.stdin.readline

INF = 1e9
N, E = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

v1, v2 = map(int, input().split())


def solve(start, target):
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (start, 0))

    # 최악의 경우 각각의 간선마다 업데이트가 발생 -> 최대 E번 반복
    # E개의 원소에 대해 우선순위 큐 작업을 한다면 O(log|E|)
    # 따라서 시간복잡도는 O(ElogE) => O(ElogV)
    while q:
        s, distance = heapq.heappop(q)
        if dist[s] < distance:
            continue

        for e, weight in adj[s]:
            cost = distance + weight
            if cost < dist[e]:
                dist[e] = cost
                heapq.heappush(q, (e, cost))

    return dist[target], dist[1], dist[N]


v1_to_v2, v1_to_one, v1_to_N = solve(v1, v2)
v1_to_v2, v2_to_one, v2_to_N = solve(v2, v1)

res = min(
    v1_to_v2 + v1_to_one + v2_to_N,  # 1 -> v1 -> v2 -> N
    v1_to_v2 + v1_to_N + v2_to_one  # 1 -> v2 -> v1 -> N
)
print(res if res < INF else -1)
