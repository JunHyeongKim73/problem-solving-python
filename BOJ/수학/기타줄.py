import sys

input = sys.stdin.readline

N, M = map(int, input().split())

min_p = 10000
min_n = 10000
for _ in range(M):
    p, n = map(int, input().split())
    min_p = min(min_p, p)
    min_n = min(min_n, n)

print(min(min_p * (N // 6) + min_n * (N % 6), min_p * (N // 6 + 1), min_n * N))
