import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def bfs(x, y):
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        nowx,nowy = queue.popleft()
        for i in range(8):
            nx = nowx + dx[i]
            ny = nowy + dy[i]
            if 0<=nx<m and 0<=ny<n and visited[nx][ny] == False and l[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))

m, n = map(int, input().split())
l = []
cnt = 0
visited = [[False]*n for _ in range(m)]
for _ in range(m):
    l.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        if visited[i][j] == False and l[i][j] == 1:
            bfs(i,j)
            cnt += 1

print(cnt)
