import sys
input = sys.stdin.readline

N, M = map(int, input().split())
before = []
after = []
for _ in range(N):
    l = input().strip()
    ll = []
    for n in l:
        ll.append(int(n))
    before.append(ll)
for _ in range(N):
    l = input().strip()
    ll = []
    for n in l:
        ll.append(int(n))
    after.append(ll)


def check(a, b):
    for j in range(b, b+3):
        if before[a][j] != 1 - after[a][j]:
            return False
    return True


def swap(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            before[i][j] = 1 - before[i][j]


def check_all():
    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]:
                return False
    return True


res = 0
for i in range(N-2):
    for j in range(M-2):
        if before[i][j] != after[i][j]:
            swap(i, j)
            res += 1

if check_all():
    print(res)
else:
    print(-1)

'''
3 4
0101
0000
0000
0010
0111
0111
'''