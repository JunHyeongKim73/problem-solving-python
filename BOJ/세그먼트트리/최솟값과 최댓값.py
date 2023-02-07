import sys

input = sys.stdin.readline

INF = 2e9
N, M = map(int, input().split())


def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = int((start + end) / 2)
    tree[node] = min(init(arr, tree, node * 2, start, mid), init(arr, tree, node * 2 + 1, mid + 1, end))
    return tree[node]


def query(tree, node, start, end, left, right):
    if left > end or start > right:
        return INF

    if left <= start and end <= right:
        return tree[node]

    mid = int((start + end) / 2)
    return min(query(tree, node * 2, start, mid, left, right), query(tree, node * 2 + 1, mid + 1, end, left, right))


plus_nums = []
minus_nums = []

for i in range(1, N + 1):
    num = int(input())
    plus_nums.append(num)
    minus_nums.append(-num)

plus_trees = [INF for _ in range(4 * N)]
minus_trees = [INF for _ in range(4 * N)]

init(plus_nums, plus_trees, 1, 0, N - 1)
init(minus_nums, minus_trees, 1, 0, N - 1)

for _ in range(M):
    a, b = map(int, input().split())
    min_num = query(plus_trees, 1, 0, N - 1, a - 1, b - 1)
    max_num = -query(minus_trees, 1, 0, N - 1, a - 1, b - 1)
    print(min_num, max_num)
