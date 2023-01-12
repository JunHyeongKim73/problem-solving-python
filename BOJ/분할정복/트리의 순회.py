import sys
input = sys.stdin.readline

n = int(input())
inorders = list(map(int, input().split()))
indexs = [0 for _ in range(n+1)]
for i in range(n):
    indexs[inorders[i]] = i
postorders = list(map(int, input().split()))

def solve():
    stack = [(0, n-1, 0, n-1)]
    while stack:
        il, ih, pl, ph = stack.pop()

        if il > ih or pl > ph:
            continue

        root = postorders[ph]
        root_idx = indexs[root]
    
        print(root, end=' ')

        # 오른쪽
        stack.append((root_idx+1, ih, pl + (root_idx - il), ph - 1))

        # 왼쪽
        stack.append((il, root_idx-1, pl, ph - (ih - root_idx + 1)))
    
    print()

solve()

'''
9
6 1 8 7 9 3 2 5 4
6 8 9 7 1 2 3 4 5
'''