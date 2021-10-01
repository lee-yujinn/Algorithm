def solution(lottos, win_nums):
    answer = []
    min = 7-len(list(set(lottos)&set(win_nums)))
    max = min-lottos.count(0)
    if min == 7 and max == 7:
        return [6,6]
    answer.append(max)
    answer.append(6) if min > 6 else answer.append(min)
    return answer
