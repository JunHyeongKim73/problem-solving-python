from sys import stdin
input = stdin.readline
t = int(input())

def solve():
	str = input()
	c = input().rstrip()

	for i in range(len(str)):
		if i%2==1:
			continue
			
		if str[i] == c:
			print('YES')
			return

	print('NO')

for _ in range(t):
	solve()
			
