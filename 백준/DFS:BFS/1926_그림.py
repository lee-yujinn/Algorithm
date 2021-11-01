import sys
from collections import  deque
input = sys.stdin.readline
sys.setrecursionlimit(3000000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
w = [0]
queue = deque()

def bfs(x,y):
    width = 0
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m and not visited[nx][ny] and g[nx][ny] == 1:
                visited[nx][ny] = True
                width += 1
                queue.append((nx, ny))
    w.append(width)
    return 1

n, m = map(int, input().split())
g = []
count = 0
visited = [[False]* m for _ in range(n)]

for _ in range(n):
    g.append(list(map(int, input().split())))

for i in range(n):
        for j in range(m):
            if not visited[i][j] and g[i][j] == 1:
                count += bfs(i,j)
print(count)
if len(w) == 1 : print(0)
else: print(max(w)+1)
