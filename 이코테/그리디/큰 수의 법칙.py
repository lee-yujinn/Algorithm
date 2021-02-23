m,n,k = map(int, input().split())
num = list(map(int, input().split()))

num.sort(reverse = True)
result = 0
while(k<n):
    if n-k > 0:
        result += num[0]*k
        n -= k
    else:
        result += num[0]*n
    result += num[1]
    n -= 1

print(result)
