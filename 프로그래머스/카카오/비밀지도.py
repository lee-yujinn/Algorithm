def solution(n, arr1, arr2):
    answer = []
    
    arr1_2 = []
    arr2_2 = []
    answer1 = ""
    
    for value in arr1:
        arr1_2.append(('{0:0%db}'%n).format(value))
    for value in arr2:
        arr2_2.append(('{0:0%db}'%n).format(value))
        
    for i in range(n):
        answer1 = ""
        for j in range(n):
            if str(arr1_2[i])[j] == '1' or str(arr2_2[i])[j] == '1':
                answer1 += '#'
            else:
                answer1 += ' '
        answer.append(answer1)
    return answer
