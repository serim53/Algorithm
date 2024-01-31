from itertools import permutations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
weight = list(map(int, input().split()))
result = 1e9

for permu in permutations(weight, n):
    num = 1
    idx = 0
    sum_weight = 0
    while num <= k:
        sum_temp = 0
        while True:
            if sum_temp + permu[idx % n] > m:
                break
            sum_temp += permu[idx % n]
            idx += 1
        num += 1
        sum_weight += sum_temp
    result = min(result, sum_weight)

print(result)