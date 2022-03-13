from sys import stdin

n = int(input())
tri = [[] for _ in range(n)]

for i in range(n):
	tri[i] = list(map(int, stdin.readline().split()))

cache = [[-1 for _ in range(i+1)] for i in range(n)]
cache[0][0] = tri[0][0]

def solve(h, idx):
	val = tri[h][idx]
	# 기저 조건
	if cache[h][idx] != -1:
		return cache[h][idx]
	# 예외 케이스 1
	if idx == 0:
		return val + solve(h-1, idx)
	# 예외 케이스 2
	if idx == h:
		return val + solve(h-1, idx-1)
	# 대각선 오른쪽 위로 갔을 때와 대각선 왼쪽 위로 갔을 때를 비교
	cache[h][idx] = max(val + solve(h-1, idx), val + solve(h-1, idx-1))
	return cache[h][idx]
	
maxs = -1
for i in range(n):
	maxs = max(maxs, solve(n-1, i))

print(maxs)