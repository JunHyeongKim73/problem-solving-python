import sys

input = sys.stdin.readline

N = int(input())


def check(n):
    if n < 100:
        return True

    l = []
    while n > 0:
        d = n % 10
        n = n // 10
        l.append(d)

    dist = l[1] - l[0]
    for i in range(1, len(l)-1):
        if l[i+1] - l[i] != dist:
            return False

    return True


res = 0
for i in range(1, N + 1):
    if check(i):
        res += 1

print(res)
