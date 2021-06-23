import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    cnt = 0
    n,m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx_que = deque(list(range(n)))

    while True:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            if idx_que.popleft() == m:
                print(cnt)
                break
        else:
            q.append(q.popleft())
            idx_que.append(idx_que.popleft())


