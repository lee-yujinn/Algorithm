from collections import Counter

def solution(participant, completion):
    part = Counter(participant)
    comp = Counter(completion)
    diff = part - comp
    
    return list(diff)[0]
