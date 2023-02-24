import sys
input = sys.stdin.readline

X, K = map(int, input().split())
X_b, K_b = bin(X)[2:], bin(K)[2:]

l = []
point = len(X_b) - 1
for i in range(len(K_b)-1, -1, -1):
    while point >= 0:
        if X_b[point] != '1':
            point -= 1
            break

        l.append('0')
        point -= 1

    l.append(K_b[i])

l.reverse()
bins = ''.join(l)
print(int(bins, 2))

'''
5 1
5 5
10 3
17 17
'''