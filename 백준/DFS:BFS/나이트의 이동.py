import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x,start_y):
    queue = deque()
    queue.append((start_x,start_y))
    while queue:
        x, y = queue.popleft()
        if x == end_x and y == end_y:
            return time[x][y]
        for next_x in (x-2,x-1,x+1,x+2):
            if next_x == x+1 or next_x == x-1:
                for next_y in (y+2, y-2):
                    if 0<= next_x < l and 0<= next_y < l and time[next_x][next_y] == 0:
                        time[next_x][next_y] = time[x][y] + 1
                        queue.append((next_x,next_y))
            elif next_x == x+2 or next_x == x-2:
                for next_y in (y+1, y-1):
                    if 0<= next_x < l and 0<= next_y < l and time[next_x][next_y] == 0:
                        time[next_x][next_y] = time[x][y] + 1
                        queue.append((next_x,next_y))

n = int(input())
result = []
for _ in range(n):
    l = int(input())
    time = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    result.append(bfs(start_x,start_y))
for v in result:
    print(v)

