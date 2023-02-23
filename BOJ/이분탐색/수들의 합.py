import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split())
l = list(map(int, input().split()))

sums = 0
for i in range(len(l)):
    sums += l[i]
    l[i] = sums

res = 0
before = 0
for i in range(len(l)):
    l_idx = bisect.bisect_left(l, before + M)
    r_idx = bisect.bisect_right(l, before + M)
    if l_idx != r_idx:
        res += 1
    before = l[i]

print(res)

'''
10 2
1 2 3 4 2 5 3 1 1 2
'''