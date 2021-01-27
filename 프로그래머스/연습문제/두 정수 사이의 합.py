def solution(a, b):
    return sum(range(a if a < b else b, a+1 if a > b else b+1))
