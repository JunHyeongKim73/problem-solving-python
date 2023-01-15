import sys

input = sys.stdin.readline

N, M = map(int, input().split())
knows = list(map(int, input().split()))
knows = set(knows[1:])


def check(p_list):
    for p_n in p_list:
        if p_n in knows:
            return False

    return True


def solve(p_input):
    ans = 0
    for p in p_input:
        if check(p):
            ans += 1

        else:
            knows.update(p)

    return ans


p_input = list()
for i in range(M):
    p = list(map(int, input().split()))
    p = p[1:]
    p_input.append(p)

for i in range(M):
    ans = solve(p_input)

print(ans)
