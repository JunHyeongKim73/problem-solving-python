import sys
input = sys.stdin.readline


def solve(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    if len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return

    root_idx = inorder.index(preorder[0])
    left_inorder = inorder[:root_idx]
    left_preorder = preorder[1:len(left_inorder)+1]
    solve(left_preorder, left_inorder)

    right_inorder = inorder[root_idx+1:]
    right_preorder = preorder[len(left_preorder)+1:]
    solve(right_preorder, right_inorder)

    print(preorder[0], end=' ')


T = int(input())
for _ in range(T):
    n = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))

    solve(pre_order, in_order)
    print()

'''
2
4
3 2 1 4
2 3 4 1
8
3 6 5 4 8 7 1 2
5 6 8 4 3 1 2 7

1
8
3 6 5 4 8 7 1 2
5 6 8 4 3 1 2 7
'''