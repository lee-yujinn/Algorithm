from collections import Counter

def solution(N, stages):
    answer = []
    fail = Counter(stages)
    num = len(stages)
    answer2 = {}
    
    for i in range(N):
        if num == 0:
            answer2[i+1] = 0
            continue
        answer2[i+1] = (fail[i+1]/num)
        num -= fail[i+1]

    return sorted(answer2, key=lambda k : answer2[k], reverse=True)
