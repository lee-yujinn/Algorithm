import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, d):
    count = 0
    queue = deque()
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

t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    d = {}

    for i in range(n):
        d[i+1] = set()

    for i in range(m):
        i, v = map(int, input().split())
        d[v].add(i)
        d[i].add(v)

    r = 0

    visited = [False] * (n + 1)

    for i in range(1,n+1):
        if visited[i] == False:
            r += bfs(i,d)
    result.append(r)

for v in result:
    print(v)
