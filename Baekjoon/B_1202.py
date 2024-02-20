import heapq

n, k = map(int, input().split())
jewel = []
bag = []
for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))
for _ in range(k):
    bag.append(int(input()))
bag.sort()
result = 0
temp = []   # 가방에 넣을 수 있는 보석의 가격 (= 가방의 무게보다 무게가 적은 보석의 가격)
for b in bag:
    while jewel and b >= jewel[0][0]:
        # 최대힙 생성
        heapq.heappush(temp, -heapq.heappop(jewel)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not jewel:
        break
print(result)