import heapq
import sys
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        heapq.heappush(right_heap, -num)
    else:
        heapq.heappush(left_heap, num)

    if right_heap and left_heap and -right_heap[0] > left_heap[0]:
        max_val = -heapq.heappop(right_heap)
        min_val = -heapq.heappop(left_heap)

        heapq.heappush(right_heap, min_val)
        heapq.heappush(left_heap, max_val)

    print(-right_heap[0])
