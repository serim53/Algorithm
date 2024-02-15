n = int(input())
building = list(map(int, input().split()))
result = [0] * n

for i in range(n - 1) :
  max_slope = -1e9
  for j in range(i + 1, n) :
    slope = (building[j] - building[i]) / (j - i)
    if slope <= max_slope :
      continue
    max_slope = max(max_slope, slope)
    result[i] += 1
    result[j] += 1

print(max(result))