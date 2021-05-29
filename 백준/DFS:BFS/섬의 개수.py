import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,-1,-1,1]

def bfs(start_x,start_y,graph,visited):
    queue.append((start_x,start_y))
    visited[start_x][start_y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return 1

result = []
while True:
    w,h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    count = 0
    visited = [[False]* w for _ in range(h)]
    for i in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and graph[i][j] == 1:
                count += bfs(i,j,graph,visited)
    result.append(count)
for v in result:
    print(v)
