import sys
from collections import deque
input = sys.stdin.readline

que = deque()

def bfs():
    que.append((S,0))
    while que:
        now, cnt = que.popleft()
        if now == G:
            return cnt
            break
        for v in [U,-D]:
            if 1 <= now + v <= F and visited[now+v] == False:
                que.append((now+v,cnt+1))
                visited[now+v] = True
    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
visited = [False] * (F+1)
print(bfs())
