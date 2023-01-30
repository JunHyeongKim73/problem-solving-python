import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

while True:
    if len(S) == len(T):
        if S == T:
            print(1)
        else:
            print(0)
        break
    last_ch = T[-1]

    T = T[:-1]
    if last_ch == 'B':
        T = T[::-1]
