import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())

    start = 0
    end = 0

    for _ in range(n):
        cx, cy, r = map(int, input().split())
        f1 = math.sqrt((cx-x1)**2 + (cy-y1)**2) < r
        f2 = math.sqrt((cx - x2) ** 2 + (cy - y2) ** 2) < r
        if f1 and f2:
            continue
        if f1:
            start += 1
        if f2:
            end += 1

    print(start + end)