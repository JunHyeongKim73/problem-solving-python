from sys import stdin
N = int(input())
arr = [[] for _ in range(N)]
for i in range(N):
	arr[i] = list(map(int, stdin.readline().split()))

cache = [[0, 0, 0] for _ in range(N)]

for i in range(3):
	cache[0][i] = arr[0][i]

for i in range(1, N):
	 cache[i][0] = min(cache[i-1][1] + arr[i][0], cache[i-1][2] + arr[i][0])
	 cache[i][1] = min(cache[i-1][0] + arr[i][1], cache[i-1][2] + arr[i][1])
	 cache[i][2] = min(cache[i-1][1] + arr[i][2], cache[i-1][0] + arr[i][2])

print(min(cache[N-1][0], cache[N-1][1], cache[N-1][2]))