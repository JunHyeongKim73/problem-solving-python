import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def solve(x, y):
	if y == 1:
		return x % C
				
	temp = solve(x, y//2)

	# 짝수
	if y % 2 == 0:
		return temp * temp % C
	# 홀수
	else:
		return temp * temp * x % C
				
result = solve(A, B)
print(result)