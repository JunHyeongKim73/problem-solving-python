from sys import stdin

N = int(input())
lists = [[-1, -1] for _ in range(N)]

# 노드가 A부터 순차적으로 커지므로 인덱스를 이용하여 트리를 리스트로 표현할 수 있다
for i in range(N):
	root, left, right = map(str, stdin.readline().split())
	
	lists[ord(root)-ord('A')][0] = left
	lists[ord(root)-ord('A')][1] = right

def preOrder(idx: int):
	print(chr(ord('A') + idx), end='')
	if lists[idx][0] != '.':
		preOrder(ord(lists[idx][0]) - ord('A'))
	if lists[idx][1] != '.':	
		preOrder(ord(lists[idx][1]) - ord('A'))

def inOrder(idx: int):
	if lists[idx][0] != '.':
		inOrder(ord(lists[idx][0]) - ord('A'))
	print(chr(ord('A') + idx), end='')
	if lists[idx][1] != '.':	
		inOrder(ord(lists[idx][1]) - ord('A'))

def postOrder(idx: int):
	if lists[idx][0] != '.':
		postOrder(ord(lists[idx][0]) - ord('A'))
	if lists[idx][1] != '.':	
		postOrder(ord(lists[idx][1]) - ord('A'))
	print(chr(ord('A') + idx), end='')
		
preOrder(0)
print()

inOrder(0)
print()

postOrder(0)
print()