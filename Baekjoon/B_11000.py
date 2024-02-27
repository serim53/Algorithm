import heapq

n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split())))
times.sort()
room = []
heapq.heappush(room, times[0][1])
for i in range(1, n):
    if times[i][0] < room[0]:
        heapq.heappush(room, times[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, times[i][1])
print(len(room))