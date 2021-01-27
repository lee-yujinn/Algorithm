def solution(strings, n):
    return sorted(strings, key=lambda strings : (strings[n], strings))
