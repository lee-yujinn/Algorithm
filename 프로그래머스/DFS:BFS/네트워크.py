def solution(n, computers):
    a = [[]for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            if computers[i][j] == 1:
                a[i].append(j)
                a[j].append(i)
    
    visited=[False]*n
    count = 0
    for i in range(n):
        if visited[i] == False:
            count += 1
            dfs(a,i,visited)
    return count

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

