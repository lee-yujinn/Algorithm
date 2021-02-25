import sys
input = sys.stdin.readline

num = int(input())
stair = [0 for _ in range(num+3)]
d = [0 for _ in range(num+3)]

for i in range(1, num+1):
    stair[i] = int(input())

d[1] = stair[1]
d[2] = stair[2]+stair[1]
d[3] = max(stair[3]+stair[2],stair[3]+d[1])

for i in range(4, num+1):
    d[i] = max(stair[i]+stair[i-1]+d[i-3],stair[i]+d[i-2])

print(d[num])
