def solution(citations):
    for i in range(sorted(citations)[-1], 0, -1):
        if len(list(filter(lambda x: x >= i, citations))) >= i:
            return i
        
    return 0
