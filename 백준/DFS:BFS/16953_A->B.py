import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

def bfs(a, b):
    queue.append((a,1))
    while queue:
        x, cnt = queue.popleft()
        if x == b:
            return cnt
        if x*2 <= b:
            queue.append((x*2,cnt+1))
        if int(str(x)+'1') <= b:
            queue.append((int(str(x)+'1'),cnt+1))
    return -1

a, b = map(int, input().split())
print(bfs(a,b))
