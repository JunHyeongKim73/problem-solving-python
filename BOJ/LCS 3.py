import sys

MAX_LENGTH = 101
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

x = len(s1)
y = len(s2)
z = len(s3)


def LCS(s1, s2, s3):
    dp = [[[0 for _ in range(MAX_LENGTH)] for _ in range(MAX_LENGTH)] for _ in range(MAX_LENGTH)]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if s1[i] == s2[j] and s2[j] == s3[k]:
                    dp[i+1][j+1][k+1] = dp[i][j][k] + 1
                else:
                    dp[i+1][j+1][k+1] = max(dp[i][j+1][k+1], dp[i+1][j][k+1], dp[i+1][j+1][k])

    res = -1
    for j in range(y):
        for k in range(z):
            res = max(res, dp[x][j+1][k+1])
    return res


res = LCS(s1, s2, s3)
print(res)

'''
abcdofghi
dfgh
bdofgi

abcdefghijklmn
efg
bdefg

dababf
ababdf
df
'''