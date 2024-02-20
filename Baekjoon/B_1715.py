import heapq

nums = []
result = 0
n = int(input())
for _ in range(n):
    heapq.heappush(nums, int(input()))
while len(nums) > 1:
    n1 = heapq.heappop(nums)
    n2 = heapq.heappop(nums)
    heapq.heappush(nums, n1 + n2)
    result += (n1 + n2)
print(result)