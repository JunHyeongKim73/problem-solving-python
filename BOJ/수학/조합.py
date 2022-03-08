from sys import stdin
n, m = map(int, stdin.readline().strip().split())

def fact(num):
	if num == 1:
		return 1

	return num * fact(num-1)

ans = fact(n) // (fact(m) * fact(n-m))
print(ans)