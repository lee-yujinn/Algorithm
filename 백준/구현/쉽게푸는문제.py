import sys

a,b = map(int,sys.stdin.readline().split())

l = []
for i in range(1,b+1):
    l += [i]*i

print(sum(l[a-1:b]))
