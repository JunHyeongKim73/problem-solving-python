import sys
from collections import deque
input = sys.stdin.readline

in_fix = input()

OP = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}

def solve():
    post_fix = list()
    weight = 1
    stack = deque()
    for ch in in_fix:
        if 'A' <= ch and ch <= 'Z':
            post_fix.append(ch)
        
        if ch == '(':
            weight *= 10
        
        if ch == ')':
            weight /= 10

        if ch in OP:
            priority = weight * OP[ch]
            # 스택에 아무것도 없을 때
            if not stack:
                stack.append((ch, priority))
                continue
            
            # 스택에 뭔가 들어있다면
            while stack:
                op, w = stack.pop()
                # 꺼낸 연산자의 우선순위가 더 높다면 출력한다
                if w >= priority:
                    post_fix.append(op)
                # 다시 넣는다
                else:
                    stack.append((op, w))
                    break
            
            stack.append((ch, priority))
            
    
    # 스택에 남은 연산자를 모두 출력한다
    while stack:
        op, w = stack.pop()
        post_fix.append(op)

    return ''.join(post_fix)

res = solve()
print(res)