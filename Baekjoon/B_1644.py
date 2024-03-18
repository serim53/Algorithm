import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
nums = []
for i in range(2, n + 1):
    if is_prime_number(i):
        nums.append(i)

result = 0
start, end = 0, 0
while end <= len(nums):
    temp = sum(nums[start:end])
    if temp == n:
        result += 1
        start += 1
    elif temp < n:
        end += 1
    else:
        start += 1
print(result)