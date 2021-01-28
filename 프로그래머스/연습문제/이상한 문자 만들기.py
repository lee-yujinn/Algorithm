def solution(s):
    answer = ""
    split = s.split(" ")
    
    for index in range(len(split)):
        for i,v in enumerate(split[index]):
            if i % 2 == 0 : 
                answer += v.upper()
            else:
                answer += v.lower()
        if index + 1 != len(split): 
            answer += " "
    
    return answer
