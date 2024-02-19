import heapq, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    min_heap, max_heap = [], []
    visited = [0] * k
    for idx in range(k):
        cmd, n = map(str, input().split())
        if cmd == 'I':
            heapq.heappush(min_heap, (int(n), idx))
            heapq.heappush(max_heap, (-int(n), idx))
            visited[idx] = 1
        else:
            # 최댓값 삭제
            if n == '1':
                # 이미 min_heap에서 삭제된 원소이므로 pop
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
            # 최솟값 삭제
            else:
                # 이미 max_heap에서 삭제된 원소이므로 pop
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    print(-max_heap[0][0], min_heap[0][0]) if max_heap and min_heap else print('EMPTY')