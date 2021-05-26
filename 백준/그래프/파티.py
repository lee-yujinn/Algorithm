import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start,end):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        time, now = heapq.heappop(q)
        if distance[now] < time:
            continue
        for v in road[now]:
            new_time = v[1] + time
            if new_time < distance[v[0]]:
                distance[v[0]] = new_time
                heapq.heappush(q, (new_time,v[0]))
    return distance[end]

n, m, x = map(int, input().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, time = map(int, input().split())
    road[start].append((end, time))

max_time = 0
for i in range(1,n+1):
    max_time = max(max_time,dijkstra(i,x) + dijkstra(x,i))
print(max_time)
