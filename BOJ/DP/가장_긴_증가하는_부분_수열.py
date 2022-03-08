from sys import stdin
N = int(input())
A = list(map(int, stdin.readline().strip().split()))

dp = [1] * N
for i in range(N):
	for j in range(i):
		if A[j] < A[i]:
			dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))