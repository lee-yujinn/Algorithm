import sys
input = sys.stdin.readline

num = int(input())
dp = [0 for _ in range(num+3)]

dp[1] = 1
dp[2] = 2

for i in range(3,num+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[num]%10007)
