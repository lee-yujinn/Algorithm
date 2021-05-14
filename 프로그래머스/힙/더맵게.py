import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while len(scoville) >= 2:
        cnt += 1
        temp = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, temp)
        if scoville[0] >= K:
            return cnt
    if scoville[0] >= K:
        return cnt


