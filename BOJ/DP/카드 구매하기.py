import sys
input = sys.stdin.readline

N = int(input())
C = list(map(int, input().split()))
C = C[:N]

cache = [0] * N
for i in range(N):
    for j in range(i):
        cache[i] = max(cache[i], cache[j] + cache[i-1-j])

    if i < len(C):
        cache[i] = max(cache[i], C[i])

print(cache[N-1])

'''
7
1 5 7 20 24
'''