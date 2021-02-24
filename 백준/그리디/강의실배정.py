import heapq
import sys
n = int(input())
c = []
dq = []

for i in range(N):
    C.append(list(map(int, sys.stdin.readline().split())))

c.sort(key=lambda c: c[0])

for i in range(n):
    if len(dq) != 0 and dq[0] <= c[i][0]:
        heapq.heappop(dq)
    heapq.heappush(dq,c[i][0])

print(len(dq))




