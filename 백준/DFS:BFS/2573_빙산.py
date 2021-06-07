import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

dx = [-1,1,0,0]
dy = [0,0,1,-1]

#빙산 덩어리 개수 구하기
def bfs(start_x,start_y,graph,visited):
    queue.append((start_x,start_y))
    visited[start_x][start_y] = True
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return 1

#바닷물 카운팅 하기
def count(x,y):
    if graph[x][y] == 0:
        return 0
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            count += 1
    return count


n, m = map(int, input().split())
graph = [] * n
year = 0
temp = [[0]*m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))

while True:
    cnt = 0
    breakp = False
    end = False
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if visited[i][j] == False and graph[i][j] != 0:
                cnt += bfs(i, j, graph, visited)

    y = year
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                end = True
                year = 0
            else:
                end = False
                breakp = True
                year = y
                break
        if breakp:
            break


    if end or cnt >= 2 or cnt == 0:
        break

    temp_graph = graph
    
    for i in range(n):
        for j in range(m):
            temp[i][j] = count(i,j)
            if graph[i][j]-temp[i][j] < 0:
                temp_graph[i][j] = 0
            else:
                temp_graph[i][j] -= temp[i][j]

    graph = temp_graph

    year += 1

print(year)
