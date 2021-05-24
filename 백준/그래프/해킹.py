import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    count = 0
    max_time = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))
    for v in distance:
        if not v == INF:
            count += 1
            max_time = max(max_time,v)
    return (count, max_time)

t = int(input())
result = []
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    result.append(dijkstra(c))

for v in result:
    print(v[0],v[1])
