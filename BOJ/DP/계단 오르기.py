import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))

INF = -1e6
cache = [[INF] * 3 for _ in range(N+1)]


def dfs(idx, nums):
    if idx > N:
        return INF

    if idx == N:
        return stairs[idx]

    if cache[idx][nums] != INF:
        return cache[idx][nums]

    if nums == 2:
        cache[idx][nums] = stairs[idx] + dfs(idx+2, 1)
        return cache[idx][nums]

    cache[idx][nums] = stairs[idx] + max(dfs(idx+1, nums+1), dfs(idx+2, 1))
    return cache[idx][nums]


ans = dfs(0, 0)
print(ans)
