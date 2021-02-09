from collections import Counter
def solution(clothes):
    key = [i[1] for i in clothes]
    count = 1
    
    for _,v in Counter(key).items():
        if len(Counter(key).items()) == 1:
            count = len(clothes)+1
        else:
            count *= (v+1)
    return count-1
