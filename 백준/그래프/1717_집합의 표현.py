import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 부모 노드를 찾는 함수
def getParent(parent, x):
    if parent[x] == x: return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

# 두 부모 노드를 합치는 함수
def unionParent(parent, a, b):
    a = getParent(parent,a)
    b = getParent(parent,b)
    if a < b: parent[b] = a
    else: parent[a] = b

# 같은 부모를 가지는지 확인
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b : print("YES")
    else: print("NO")

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    n, a, b = map(int, input().split())
    if n == 0: unionParent(parent, a, b)
    else: findParent(parent, a, b)
