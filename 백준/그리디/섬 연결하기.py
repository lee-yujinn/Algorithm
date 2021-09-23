def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    c = set([costs[0][0],costs[0][1]])
    answer, visited = costs[0][2], [False] * n
    visited[0] = True
    
    while len(c) != n:
        for i in range(1,len(costs)):
            if costs[i][0] in c and costs[i][1] in c:
                continue
            if costs[i][0] in c or costs[i][1] in c:
                c.update([costs[i][0],costs[i][1]])
                answer += costs[i][2]
                break
            
    return answer
