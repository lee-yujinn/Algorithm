def solution(numbers):
    answer = []

    for i in range(0,len(numbers)):
        for j in range(0,len(numbers)):
            if i != j:
                answer.append(numbers[i]+numbers[j])

    answer = list(set(answer))
    answer.sort()

    return answer
