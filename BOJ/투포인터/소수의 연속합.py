import sys
from math import sqrt
from collections import deque

input = sys.stdin.readline

N = int(input())

dq = deque()

sums = 0
res = 0


def get_primary(n):
    lists = [True] * (n+1)
    for i in range(2, int(sqrt(n)) + 1):
        for j in range(2, int(n/i)+1):
            lists[i*j] = False

    primary_list = []
    for i in range(len(lists)):
        if lists[i]:
            primary_list.append(i)
    return primary_list[2:]


primary_list = get_primary(N)

for i in primary_list:

    dq.append(i)
    sums += i

    if sums > N:
        while sums > N:
            n = dq.popleft()
            sums -= n

    if sums == N:
        res += 1

print(res)
