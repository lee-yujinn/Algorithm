import sys, copy
from collections import  deque
input = sys.stdin.readline
sys.setrecursionlimit(300000)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

#빙산 개수
def bfs(x,y):
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and g[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx,ny))
    return 1

#바닷물에 녹는
def melt():
    g2 = copy.deepcopy(g)
    for i in range(n):
        for j in range(m):
            if g[i][j] != 0:
                for i2 in range(4):
                    nx = i + dx[i2]
                    ny = j + dy[i2]
                    if 0 <= nx < n and 0 <= ny < m:
                        if g[nx][ny] == 0: g2[i][j] -= 1
                        if g2[i][j] == 0: break
    return g2

n, m = map(int, input().split())
year = 0
g = []

for _ in range(n):
    g.append(list(map(int, input().split())))

while True:
    visited = [[False] * m for _ in range(n)]
    c = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and g[i][j] != 0:
                c += bfs(i, j)

    if c >= 2:
        print(year)
        break
    if c == 0:
        print(0)
        break

    g = melt()
    year += 1
