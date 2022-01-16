import sys
input = sys.stdin.readline

n = int(input())

def countLeft(start, end):
    result = 0
    while start < end:
        if s[start] != s[end]:
            result += 1
            if s[start+1] == s[end]:
                start += 1
            elif s[start] == s[end-1]:
                end -= 1
        else:
            start += 1
            end -= 1
        if result >= 2: break
    return result

def countRight(start, end):
    result = 0
    while start < end:
        if s[start] != s[end]:
            result += 1
            if s[start] == s[end - 1]:
                end -= 1
            elif s[start+1] == s[end]:
                start += 1
        else:
            start += 1
            end -= 1
        if result >= 2: break
    return result

for _ in range(n):
    result = 0
    s = str(input().strip())
    start, end = 0, len(s) - 1
    print(min(countLeft(start,end),countRight(start,end)))
