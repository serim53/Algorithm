# bisect 모듈 사용
import bisect

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(1, n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))

# 이진탐색 직접구현
# def binary_search(num):
#     start, end = 0, len(dp)
#     while start <= end:
#         mid = (start + end) // 2
#         if dp[mid] < num:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return start
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# dp = [arr[0]]
#
# for i in range(1, n):
#     if arr[i] > dp[-1]:
#         dp.append(arr[i])
#     else:
#         idx = binary_search(arr[i])
#         dp[idx] = arr[i]
#
# print(len(dp))