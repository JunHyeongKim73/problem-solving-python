import sys
input = sys.stdin.readline

X = int(input())

res = 0
while True:
    a = (X & -X)
    X -= a

    res += 1
    if X == 0:
        break

print(res)