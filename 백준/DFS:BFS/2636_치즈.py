import sys, copy
from collections import  deque
input = sys.stdin.readline
sys.setrecursionlimit(300000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

def bfs(x,y):
    c = 0
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if g[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                else:
                    visited[nx][ny] = True
                    c += 1
                    g[nx][ny] -= 1
    return c

n, m = map(int, input().split())
g = []
time, count = 0, 0

for _ in range(n):
    g.append(list(map(int, input().split())))

while True:
    visited = [[False] * m for _ in range(n)]
    time += 1
    c = bfs(0,0)
    if c == 0:
        break
    else:
        count = c

print(time-1)
print(count)
