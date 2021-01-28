def solution(arr):
    arr.remove(sorted(arr)[0])
    return arr if len(arr) != 0 else [-1]
