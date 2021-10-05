import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find(parent, a):
    if parent[a] == a : return a
    parent[a] = find(parent,parent[a])
    return parent[a]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

def sameRoot(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b : return True
    else: return False

def connectRoad(parent, n):
    for i in range(1, n):
        if not sameRoot(parent, road[i - 1], road[i]): return "NO"
    return "YES"

n = int(input())
m = int(input())
parent = [0] * n
for i in range(n):
    parent[i] = i

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

for i in range(len(l)):
    for index, j in enumerate(l[i]):
        if j == 1:
            union(parent,i,index)

road = list(map(int,input().split()))
road = list(map(lambda x: x-1, road))

print(connectRoad(parent,m))
