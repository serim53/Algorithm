n = int(input())
nums = list(map(int, input().split()))
result = 0
start, end = 0, 0
visited = [0] * 100001
while start <= end < n:
    if not visited[nums[end]]:
        visited[nums[end]] = 1
        end += 1
        result += end - start
    else:
        while visited[nums[end]]:
            visited[nums[start]] = 0
            start += 1
print(result)