def solution(d, budget):
    answer = 0
    for value in sorted(d):
        if budget - value >= 0:
            budget -= value
            answer += 1
        else:
            break;
            return answer
    return answer
