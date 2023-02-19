import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

M = N
l = deque()
while M > 0:
    n = (M & -M)
    l.append(n)
    M -= n

lens = len(l)
res = 0
while lens > K:
    f = l.popleft()
    s = l.popleft()

    res += (s - f)
    l.appendleft(2*s)

    lens -= 1

if N <= K:
    print(0)
else:
    print(res)

'''
10000000 1000
'''