import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

def check(v):
    for i in range(len(v)-1):
        if v[i] != v[i+1]:
            if v[i] in v[i+1:]:
                return 0
    return 1

for _ in range(n):
    v = str(input())
    cnt += check(v)

print(cnt)
