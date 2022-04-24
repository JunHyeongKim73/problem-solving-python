from sys import stdin
input = stdin.readline
t = int(input())

def solve():
	l, r, a = map(int, input().split())
	div = r // a
	maxs = div * a - 1
	target = maxs
	if maxs < l or r == maxs + a:
		target = r
	res = target//a + target%a
	return res

for _ in range(t):
	print(solve())