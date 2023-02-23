import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
P = list(map(int, input().split()))
P = ''.join(str(e) for e in P)
d = {}


def check(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False

    return True


def swap(s, i):
    s = list(s)
    for j in range(int(K/2)):
        s[i+j], s[i+K-1-j] = s[i+K-1-j], s[i+j]
    return ''.join(s)


def solve():
    q = deque()
    q.append((P, 0))

    while q:
        s, num = q.popleft()
        if check(s):
            return num

        for i in range(N-K+1):
            ns = swap(s, i)
            if ns in d:
                continue
            d[ns] = ns
            q.append((ns, num + 1))

    return -1

res = solve()
print(res)