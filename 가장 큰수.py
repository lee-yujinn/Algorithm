def solution(numbers):
    numbers = list(map(str,numbers))
    numbers = sorted(numbers, key = lambda x : x*3, reverse = True)
    
    if numbers.count('0') == len(numbers):
        return '0'
    else:
        return ''.join(numbers)
