import heapq

def solution(jobs):
    answer = 0
    i = 0
    start = -1
    now = 0
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            p = heapq.heappop(heap)
            start = now
            now += p[0]
            answer += (now - p[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))