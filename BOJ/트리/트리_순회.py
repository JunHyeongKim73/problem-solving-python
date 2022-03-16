from sys import stdin

class Node:
    def __init__ (self,data,left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def preorder(node): # 전위순회
    if node is None: # 노드가 없을 경우 그냥 return
        return
    print(node.data, end = '') # 루트
    if node.left: # 왼쪽자식
        preorder(tree[node.left])
    if node.right: #오르쪽 자식
        preorder(tree[node.right])

def inorder(node): # 중위순회
    if node is None:
        return
    if node.left: #왼쪽자식
        inorder(tree[node.left])
    print(node.data, end='') # 루트
    if node.right: # 오른쪽
        inorder(tree[node.right])

def postorder(node): # 후위순회
    if node is None:
        return
    if node.left: # 왼쪽 자식
         postorder(tree[node.left])
    if node.right: #오른쪽 자식
        postorder(tree[node.right]) # 루트
    print(node.data, end='')


n = int(stdin.readline()) # 이진트리의 노드 개수
'''
트리를 dictionary로 표현
index로 찾는데 O(1)이 걸리므로 문제가 없음!
'''
tree = {}
for __ in range(n):
    root, left, right = stdin.readline().strip().split() # A B C (공백삭제하고 자르기)
    if left == '.': # '. ' 일 경우 비어있는 거
        left = None
    if right =='.':
        right = None
    tree[root] = Node(root,left,right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])