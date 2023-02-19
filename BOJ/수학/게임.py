import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = int(100*Y/X)


def solve(lo, hi):
    if lo >= hi:
        return lo

    mid = int((lo + hi) / 2)
    plus_z = int(100*(Y+mid)/(X+mid))

    if plus_z == Z:
        return solve(mid + 1, hi)

    return solve(lo, mid)


res = solve(1, 1e9)
if Z >= 99:
    print(-1)
else:
    print(res)