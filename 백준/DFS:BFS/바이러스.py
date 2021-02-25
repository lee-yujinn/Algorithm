n = int(input())
c = int(input())
d = {}
for i in range(n):
    d[i+1] = set()
    
for i in range(c):
    i,j = map(int,input().split())
    d[i].add(j)
    d[j].add(i)

visited = [False]*(n+1)

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
    return visited

print(dfs(d,1,visited).count(True)-1)
     

