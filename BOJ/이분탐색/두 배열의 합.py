import sys
import bisect

input = sys.stdin.readline

T = int(input())
n = int(input())
n_l = list(map(int, input().split()))
m = int(input())
m_l = list(map(int, input().split()))


def possible_list(l):
    p_l = []
    for step in range(1, len(l) + 1):
        sums = 0
        for i in range(step):
            sums += l[i]

        p_l.append(sums)
        start_idx, end_idx = 0, step
        while end_idx < len(l):
            sums -= l[start_idx]
            sums += l[end_idx]
            p_l.append(sums)
            start_idx += 1
            end_idx += 1

    return p_l


n_p_l = possible_list(n_l)
m_p_l = possible_list(m_l)

n_p_l.sort()
m_p_l.sort()

res = 0
for num in n_p_l:
    l_idx = bisect.bisect_left(m_p_l, T-num)
    r_idx = bisect.bisect_right(m_p_l, T - num)

    res += (r_idx - l_idx)

print(res)

'''
5
4
1 3 1 2
3
1 3 2
'''