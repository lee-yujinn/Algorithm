import sys
from collections import deque
input = sys.stdin.readline

que = deque()

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,matrix,visited):
    que.append((x,y))
    visited[x][y] = True
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if matrix[x][y] == matrix[nx][ny]:
                    que.append((nx,ny))
                    visited[nx][ny] = True


n = int(input())
rgb = [list(input().rstrip()) for _ in range(n)]
rgb_visited = [[False]*n for _ in range(n)]
rb_visited = [[False]*n for _ in range(n)]
rgbcnt = 0
rbcnt = 0

for i in range(n):
    for j in range(n):
        if rgb_visited[i][j] == False:
            bfs(i,j,rgb,rgb_visited)
            rgbcnt += 1

for i in range(n):
    for j in range(n):
        if rgb[i][j] == 'R':
            rgb[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if rb_visited[i][j] == False:
            bfs(i,j,rgb,rb_visited)
            rbcnt += 1

print(rgbcnt, rbcnt)
