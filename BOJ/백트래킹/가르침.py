import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())

words = []
for _ in range(N):
    s = list(set(input().strip()))
    for ch in "acint":
        s.remove(ch)
    bits = 0
    for ch in s:
        bits |= (1 << ord(ch) - 96)
    words.append(bits)

arr = [chr(97 + i) for i in range(26)]
for ch in "acint":
    arr.remove(ch)

def solve():
    if K < 5:
        return 0

    max_counts = -1
    for comb in list(combinations(arr, K - 5)):
        bits = 0
        for ch in comb:
            bits |= (1 << ord(ch) - 96)

        counts = 0
        for word in words:
            if word & bits == word:
                counts += 1

        max_counts = max(max_counts, counts)
    return max_counts


res = solve()
print(res)

'''
9 15
antabtica
antaxtica
antadtica
antaetica
antaftica
antagtica
antahtica
antajtica
antaktica
'''
