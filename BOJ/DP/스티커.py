from sys import stdin
T = int(stdin.readline())

for _ in range(T):
	n = int(stdin.readline())
	arr = [[0 for _ in range(n)] for _ in range(2)]
	for j in range(2):
		arr[j] = list(map(int, stdin.readline().split()))

	dp = [[-1 for _ in range(n)] for _ in range(2)]
	dp[0][0] = arr[0][0]
	dp[1][0] = arr[1][0]
	
	for i in range(1, n):
		if i == 1:
			dp[0][i] = dp[1][0] + arr[0][i]
			dp[1][i] = dp[0][0] + arr[1][i]
		
		else:
			dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
			dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]

	print(max(dp[0][n-1], dp[1][n-1]))	