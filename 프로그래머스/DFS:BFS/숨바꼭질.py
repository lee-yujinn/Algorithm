import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        if v == k:
            print(time[v])
            return
        for next_step in (v-1,v+1,v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v]+1
                q.append(next_step)
MAX = 100001
time = [0] * MAX

bfs()
