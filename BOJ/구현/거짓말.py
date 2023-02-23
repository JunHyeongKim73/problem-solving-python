import sys
input = sys.stdin.readline

N, M = map(int, input().split())
knows = list(map(int, input().split()))
knows = set(knows[1:])

party = []
for _ in range(M):
    l = list(map(int, input().split()))
    party.append(l[1:])


def has_know(p):
    for n in p:
        if n in knows:
            return True
    return False


for _ in range(M):
    for p in party:
        if has_know(p):
            knows.update(p)

res = 0
for p in party:
    if not has_know(p):
        res += 1

print(res)


'''
10 10
4 1 2 3 4
2 1 5
2 2 6
1 7
1 8
2 7 8
1 9
1 10
2 3 10
1 4
1 7 10
'''