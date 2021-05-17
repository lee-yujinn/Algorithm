import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
m = 0
result = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    m = max(m,max(graph[i]))

queue = deque()

def bfs(graph,start_x,start_y,max,visited):
    queue.append((start_x,start_y))
    visited[start_x][start_y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<n:
                if graph[nx][ny] > max and visited[nx][ny] == False:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
    return 1

for i in range(1,m):
    temp = 0
    visited = [[False] * n for _ in range(n)]
    for xpos in range(n):
        for ypos in range(n):
            if visited[xpos][ypos] == False and graph[xpos][ypos] > i:
                temp += bfs(graph,xpos,ypos,i,visited)
    result = max(result,temp)

print(result)
