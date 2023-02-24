import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))

order = [-1] * N
for i in range(N):
    sums = 0
    for j in range(N):
        if order[j] == -1:
            sums += 1

        if sums == l[i]+1:
            order[j] = i+1
            break


for e in order:
    print(e, end=' ')