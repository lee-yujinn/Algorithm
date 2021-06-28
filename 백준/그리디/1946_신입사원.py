import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = [[0,0] for _ in range(N)]
    cnt = 1
    for i in range(N):
        score[i][0], score[i][1] = map(int, input().split())
    score.sort()
    m = score[0][1]
    for i in range(1,N):
        m = min(m,score[i][1])
        if m == score[i][1]:
            cnt += 1
    print(cnt)

