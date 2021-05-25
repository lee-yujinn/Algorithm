import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dijkstra(x,y):
    q = []
    heapq.heappush(q,(graph[x][y],x,y))
    distance[x][y] = 0
    while q:
        cost, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            print(f'Problem {c}: {distance[x][y]}')
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                n_cost = cost + graph[nx][ny]
                if n_cost < distance[nx][ny]:
                    distance[nx][ny] = n_cost
                    heapq.heappush(q, (n_cost,nx,ny))

c = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        k = list(map(int, input().split()))
        graph.append(k)
    dijkstra(0,0)
    c += 1
