import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.sort()

mins = A[N-1] - A[0]
for i in range(N):
    idx = bisect.bisect_left(A, A[i]+M)
    if idx == N:
        continue

    diff = A[idx] - A[i]
    mins = min(mins, diff)

print(mins)
'''
7 9
1
4
6
8
17
33
65

3 3
1
5
3
'''