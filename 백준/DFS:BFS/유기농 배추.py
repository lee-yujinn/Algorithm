import sys
from collections import deque
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m or graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
    
num = int(input())
for _ in range(num):
    n,m,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    result = 0
    for _ in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    print(result)
