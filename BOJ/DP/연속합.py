import sys

input = sys.stdin.readline

# 모두 다 양수라면 다 더하는 게 맞다
# 깎이면 남겨놓는다

n = int(input())
arr = list(map(int, input().split()))

ans = -1000
sums = 0
for num in arr:
    sums += num
    ans = max(ans, sums)

    if sums < 0:
        sums = 0

print(ans)

'''
10
10 -4 3 1 5 6 -35 12 21 -1

10
2 1 -4 3 4 -4 6 5 -5 1

5
-1 -2 -3 -4 -5

5
1 2 3 4 5

4
-1000 -1000 -1000 -1000

8
67 -80 -49 79 14 -20 -35 81
'''
