def solution(people, limit):
    answer = 0
    people.sort()
    
    index1 = 0
    index2 = len(people)-1
    
    while index1 < index2:
        if people[index1]+people[index2] <= limit:
            answer += 1
            index1 += 1
            index2 -= 1
        else:
            index2 -= 1
    
    answer += len(people) - answer*2
    return answer
