def solution(n):
    answer = []
    for i in range (len(str(n))-1 ,-1,-1):
        answer.append(int(str(n)[i]))
    return answer
