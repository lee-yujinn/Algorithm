import sys

l=[]
n = int(sys.stdin.readline())
for i in range(n):
    l.append(list(map(int,sys.stdin.readline().split())))

for i in range(len(l)):
    l[i].sort(reverse=True)
    print(l[i][2])
