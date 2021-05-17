import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
queue = deque()
result = 0
change = False

def bfs():
    change = False
    while queue:
        x,y =queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and ny>=0 and nx<k and ny<n:
                if graph[nx][ny] == 0:
                    queue.append((nx,ny))
                    graph[nx][ny] += graph[x][y] + 1
                    change = True
    return change
n, k = map(int, input().split())
graph = []
for i in range(k):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))
ch = bfs()
end = False

for i in graph:
    for j in i:
        if ch == False and j != 0:
            result = 1
            end = True
            break
        if j == 0:
            result = 0
            end = True
            break
        else:
            result = max(result,j)
    if end:
        break
print(result-1)
