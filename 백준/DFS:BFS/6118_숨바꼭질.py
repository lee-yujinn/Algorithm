import sys
from collections import  deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] += visited[v] + 1

n, m = map(int, input().split())
visited = [0] * (n+1)
d = {}

for _ in range(m):
    a, b = map(int, input().split())
    d.setdefault(a, []).append(b)
    d.setdefault(b, []).append(a)

bfs(d,1,visited)
m = max(visited)

print(visited.index(m),m-1,visited.count(m))
