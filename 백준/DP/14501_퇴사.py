import sys
input = sys.stdin.readline

n = int(input())
t, p, d = [0] * (n+1), [0] * (n+1), [0] * (n+1)

for i in range(n):
    t[i],p[i] = map(int, input().split())

for i in range(len(t)-2, -1, -1):
    if t[i]+i <= n:
        d[i] = max(p[i]+d[i+t[i]],d[i+1])
    else:
        d[i] = d[i+1]

print(d[0])
