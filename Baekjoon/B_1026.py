n = int(input())

nums_a = list(map(int, input().split()))
nums_b = list(map(int, input().split()))

sorted_a = sorted(nums_a, reverse=True)
sorted_b = sorted(nums_b)

s = 0
for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)