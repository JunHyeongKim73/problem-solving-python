import sys
import heapq
input = sys.stdin.readline

hq = []

N = int(input())
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(hq) == 0:
            print(0)
            continue

        print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, x)
