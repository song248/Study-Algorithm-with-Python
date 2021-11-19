import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        count += 1
    return count if scoville[0] >= K else -1