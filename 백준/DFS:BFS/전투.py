from collections import deque

m, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
w,b=0,0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,team):
    queue = deque()
    queue.append((x,y))
    count = 0
    graph[x][y] == 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] == team:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                count += 1
    return (1 if count==0 else count)


for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            if graph[i][j] == 'W':
                w += bfs(i,j,graph[i][j])**2
            else:
                b += bfs(i,j,graph[i][j])**2
print(w,b)
