import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = list(map(int, input().split()))
c = []
cnt = 0

for i in range(K):
    if l[i] in c:
        continue
    if len(c) < N:
        c.append(l[i])
        continue
    idxs = []

    for j in range(N):
        try:
            idx = l[i:].index(c[j])
        except:
            idx = 101
        idxs.append(idx)
    del c[idxs.index(max(idxs))]
    c.append(l[i])
    cnt += 1

print(cnt)
