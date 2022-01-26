import sys

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]

house.sort()

start = 1
end = house[-1] - house[0]
result = []

while start <= end:
    count = 1
    mid = (start + end) // 2
    current = house[0]
    for x in house:
        if current + mid <= x:
            count += 1
            current = x
    if count >= C:
        start = mid + 1
        result.append(mid)
    else:
        end = mid - 1

print(max(result))