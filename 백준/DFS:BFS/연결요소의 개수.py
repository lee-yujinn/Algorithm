import sys
from collections import deque
input = sys.stdin.readline
n,c = map(int, input().split())
d = {}
for i in range(n):
    d[i + 1] = set()

for i in range(c):
    i, j = map(int, input().split())
    d[i].add(j)
    d[j].add(i)

visited = [False] * (n+1)
visited[0] = True
count = 0

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        value = queue.popleft()
        for v in graph[value]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    return 1

for i in range(1,n+1):
    if not visited[i] == True:
        count += bfs(d,i,visited)
print(count)
