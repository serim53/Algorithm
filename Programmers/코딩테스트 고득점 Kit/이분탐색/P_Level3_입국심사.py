def solution(n, times):
    left, right = 1, max(times) * n
    times.sort()
    while left <= right:
        mid = (left + right) // 2
        num = 0
        for time in times:
            num += mid // time
            if num >= n:
                break
        if num >= n:
            right = mid - 1
        elif num < n:
            left = mid + 1
    return left