from heapq import heappop, heappush

def solution(book_time):
    answer = 1

    book_info = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_info.sort()

    heap = []
    for s, e in book_info:
        if not heap:
            heappush(heap, e + 10)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap, e + 10)

    return answer