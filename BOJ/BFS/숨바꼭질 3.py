import sys
from sys import stdin
from queue import PriorityQueue

N, K = map(int, stdin.readline().strip().split())

q = PriorityQueue()
visited = [False] * 100001

def solve(n, k):

    q.put((0, k))

    while not q.empty():
        sec, nk = q.get()
        
        if nk == -1 or nk == 100001:
            continue

        if visited[nk]:
            continue
        
        visited[nk] = True

        if n == nk:
            return sec

        if nk % 2 == 0: # 짝수
            q.put((sec+1, nk-1))
            q.put((sec+1, nk+1))
            q.put((sec, int(nk/2)))
            
        else: # 홀수
            q.put((sec+1, nk-1))
            q.put((sec+1, nk+1))

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    res = solve(N, K)
    
    print(res)