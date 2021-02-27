import sys
input = sys.stdin.readline

n = int(input())
l = [0]
dp = [0] * (n+1)
for i in range(n):
    l.append(list(map(int, input().split())))

for i in range(1,n):
    if i + l[i][0]<=n:
        dp[i+l[i][0]] = max(dp[i+l[i][0]],l[i][1])
    else:
        dp[i] = dp[i-1]
print(dp)
