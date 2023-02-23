import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = int(100 * Y / X)


def solve(lo, hi):
    if lo >= hi:
        return lo

    mid = int((lo + hi) / 2)
    if int(100 * (Y+mid)/(X+mid)) > Z:
        return solve(lo, mid)
    else:
        return solve(mid + 1, hi)


res = solve(0, 1e9)

if Z >= 99:
    print(-1)
else:
    print(res)