def solution(n, lost, reserve):
    for i in lost[:] :
        if i in reserve[:] :
            reserve.remove(i)
            lost.remove(i)
    answer = n - len(lost)
    print(reserve, lost)
    for i in reserve :
        if i-1 in lost :
            answer+=1
            lost.remove(i-1)
        elif i+1 in lost :
            answer+=1
            lost.remove(i+1)  
    
    return answer
