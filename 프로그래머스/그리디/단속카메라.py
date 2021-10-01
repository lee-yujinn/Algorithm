def solution(routes):
    answer = 0
    c = -31000
    routes.sort(key = lambda x: x[1])
    
    for v in routes:
        if c < v[0]:
            answer += 1
            c = v[1]
    return answer


