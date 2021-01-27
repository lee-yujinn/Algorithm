def solution(arr, divisor):
    answer = []
    answer = sorted([i for i in arr if i % divisor == 0])
    return [-1] if len(answer) == 0 else answer
