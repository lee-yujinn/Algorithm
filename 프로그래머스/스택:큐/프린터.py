from collections import deque

def solution(priorities, location):
    answer = 0
    d = deque([(v,i) for i,v in enumerate(priorities)])

    while d:
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
            print(d)
        else:
            answer += 1
            if item[1] == location:
                break
                
    return answer
