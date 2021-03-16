import sys
from collections import deque
sys.setrecursionlimit(100000)

input = sys.stdin.readline
l = []

def dfs(x,y,count):
    if x<0 or y<0 or x>=num or y>=num or graph[x][y] == 0:
        return 0
    if graph[x][y] == '1':
        graph[x][y] = 0
        count +=1 
        dfs(x-1,y,count)
        dfs(x,y-1,count)
        dfs(x+1,y,count)
        dfs(x,y+1,count)
        l.append(count+1)
        return count
    return count
    
num = int(input())
for _ in range(num):
    graph = [list(input().strip()) for _ in range(num)]
    result = 0
    for i in range(num):
        for j in range(num):
            k = dfs(i,j,0)
            if k > 0:
                result += 1
    print(result)
    print(sorted(l))
