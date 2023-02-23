import sys
input = sys.stdin.readline

K, S, N = map(str, input().split())

N = int(N)
kr, kc = ord(K[0])-ord('A'), int(K[1])-1
sr, sc = ord(S[0])-ord('A'), int(S[1])-1

d = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1],
    'LB': [-1, -1]
}

for _ in range(N):
    c = input().strip()
    nkr = kr + d[c][0]
    nkc = kc + d[c][1]
    if nkr == -1 or nkr == 8 or nkc == -1 or nkc == 8:
        continue

    if nkr == sr and nkc == sc:
        nsr = sr + d[c][0]
        nsc = sc + d[c][1]
        if nsr == -1 or nsr == 8 or nsc == -1 or nsc == 8:
            continue

        sr = nsr
        sc = nsc

    kr = nkr
    kc = nkc

print(chr(kr + 65) + str(kc+1))
print(chr(sr + 65) + str(sc+1))