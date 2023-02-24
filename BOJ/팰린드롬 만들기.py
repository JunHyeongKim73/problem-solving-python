import sys
input = sys.stdin.readline

S = input().strip()

def check(s):
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            return False

    return True

maxs = 1
for i in range(len(S)):
    temp = S[i:]

    if check(temp):
        maxs = max(maxs, len(S)-i)

add_to = len(S) - maxs
print(len(S) + add_to)