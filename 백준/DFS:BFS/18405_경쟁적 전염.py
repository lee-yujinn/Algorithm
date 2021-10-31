import sys
from collections import  deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(s):
  q = deque(v)
  count = 0
  while q:
    if count == s: break
    for _ in range(len(q)):
      x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
          if g[nx][ny] == 0:
            g[nx][ny] = g[x][y]
            q.append((nx, ny))
    count += 1

n, k = map(int, input().split())
g = []
v = []
for i in range(n):
    g.append(list(map(int, input().split())))
    for j in range(len(g[i])):
        if not g[i][j] == 0:
            v.append((i,j))

s, x, y = map(int, input().split())
v.sort()

bfs(s)
print(g[x-1][y-1])
