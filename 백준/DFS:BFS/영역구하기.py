import sys
from collections import deque
input = sys.stdin.readline

m,n,k = map(int,input().split())
l = []
graph = [[1] * m for _ in range(n)]
for i in range(k):
    l.append(list(map(int,input().split())))

for i in range(k):
    for x in range(l[i][0],l[i][2]):
        for y in range(l[i][1],l[i][3]):
            graph[x][y] = 0

nx = [1,-1,0,0]
ny = [0,0,1,-1]
queue = deque()

def bfs(x,y,visited):
    queue.append((x,y))
    visited[x][y] = True
    width = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx>=0 and dy>=0 and dx<n and dy<m and visited[dx][dy] == False and graph[dx][dy] == 1:
                queue.append((dx,dy))
                visited[dx][dy] = True
                width += 1
    return width

visited = [[False] * m for _ in range(n)]
count = 0
result = []
for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j] == 1:
            count += 1
            result.append(bfs(i,j,visited)+1)

print(count)
result.sort()
for v in result:
    print(v, end = ' ')
