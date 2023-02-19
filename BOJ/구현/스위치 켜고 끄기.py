import sys
input = sys.stdin.readline

N = int(input())
s = list(map(int, input().split()))

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        sums = b
        while sums <= N:
            s[sums-1] = 1 - s[sums-1]
            sums += b
    else:
        s[b-1] = 1 - s[b-1]
        for i in range(1, N):
            l = b-1-i
            r = b-1+i
            if l == -1 or r == N:
                break
            if s[l] != s[r]:
                break
            s[l] = 1 - s[l]
            s[r] = 1 - s[r]

for i in range(len(s)):
    print(s[i], end=' ')
    if i % 20 == 19:
        print()

'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3

21
0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 1 1 1
2
1 3
2 3
'''