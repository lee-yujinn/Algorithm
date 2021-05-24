import sys
from collections import deque
input = sys.stdin.readline

def bfs(start,d):
    count = 0
    queue = deque()
    visited = [False] * (n + 1)
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for value in d[v]:
            if not visited[value]:
                queue.append(value)
                visited[value] = True
                count += 1
    return count

n, m = map(int, input().split())
d = {}

for i in range(n):
    d[i+1] = set()

for _ in range(m):
    index, value = map(int, input().split())
    d[value].add(index)

result = []

for i in range(1,n+1):
   result.append(bfs(i,d))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i+1, end= ' ')
