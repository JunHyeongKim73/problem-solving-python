import sys
input = sys.stdin.readline

N = int(input())
l = list(set(map(int, input().split())))
l.sort()

for i in l:
    print(i, end=" ")