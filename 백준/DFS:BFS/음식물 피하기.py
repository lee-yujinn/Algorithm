from collections import deque
import sys

n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
result = 0

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    graph[r-1][c-1] = 1


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 3
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 3
                cnt += 1
    return (1 if cnt==0 else cnt)

for i in range(n):
    for j in range(m):
        if not graph[i][j] == 3:
            k = bfs(i,j)
            if k > result:
                result = k
print(result)
