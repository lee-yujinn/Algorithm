from collections import Counter

def solution(s):
    return True if Counter(s.upper())['P'] == Counter(s.upper())['Y'] else False
