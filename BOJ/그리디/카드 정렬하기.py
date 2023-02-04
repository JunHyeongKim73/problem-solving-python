import sys
import heapq
input = sys.stdin.readline

pq = []
N = int(input())
for _ in range(N):
    num = int(input())
    heapq.heappush(pq, num)

res = 0
while len(pq) >= 2:
    first_smallest = heapq.heappop(pq)
    second_smallest = heapq.heappop(pq)
    add = first_smallest + second_smallest

    res += add
    heapq.heappush(pq, add)

print(res)
