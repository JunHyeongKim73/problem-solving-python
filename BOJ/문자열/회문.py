import sys
input = sys.stdin.readline


def is_palindrome(S):
    for i in range(len(S)//2):
        if S[i] != S[-(i+1)]:
            return False

    return True


def is_pseudo_pal(S):
    idx = -1
    for i in range(len(S)//2):
        if S[i] != S[-(i+1)]:
            idx = i
            break

    if is_palindrome(S[(idx+1):(-idx or None)]):
        return True
    if is_palindrome(S[idx:-(idx+1)]):
        return True

    return False


T = int(input())
for _ in range(T):
    S = input().strip()
    if is_palindrome(S):
        print(0)
    elif is_pseudo_pal(S):
        print(1)
    else:
        print(2)

'''
2
xaxxa
bxaxxab
'''