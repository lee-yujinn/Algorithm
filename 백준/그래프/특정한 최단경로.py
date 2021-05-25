import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start,end):
    q = []
    heapq.heappush(q,(0,start))
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v in graph[now]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))
    return distance[end]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int, input().split())

p1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2, n)
p2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1, n)

if p1 >= INF and p2 >= INF:
    print(-1)
else:
    print(min(p1,p2))
