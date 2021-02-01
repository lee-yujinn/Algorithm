def solution(x, n):
    answer = [x]
    value = x
    for _ in range(n-1):
        answer.append(value+x)
        value += x
    return answer
