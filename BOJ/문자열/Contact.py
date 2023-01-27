import sys
import re
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().rstrip()
    regex = re.compile("(100+1+|01)+")
    if regex.fullmatch(s):
        print("YES")
    else:
        print("NO")