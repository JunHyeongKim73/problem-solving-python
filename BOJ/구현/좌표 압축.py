import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
sorted_X = sorted(X)

d = dict()
index = 0
prev_num = 1e10
for n in sorted_X:
    if prev_num == n:
        continue

    d[n] = index
    index += 1
    prev_num = n

for num in X:
    print(d[num], end=' ')
