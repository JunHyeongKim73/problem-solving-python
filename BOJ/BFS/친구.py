import sys
input = sys.stdin.readline

N = int(input())
t = []
for _ in range(N):
    t.append(input().strip())


res = [0]*N
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if t[i][j] == 'Y':
            res[i] += 1
        else:
            for k in range(N):
                if t[j][k] == 'Y' and t[k][i] == 'Y':
                    res[i] += 1
                    break

print(max(res))
'''
3
NYY
YNY
YYN
'''