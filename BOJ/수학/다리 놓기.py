import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    res = int(math.factorial(M)/(math.factorial(N)*math.factorial(M-N)))
    print(res)