from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        now = prices.popleft()
        time = 0
        for p in prices:
            if now > p:
                time += 1
                break
            time += 1
        answer.append(time)
    return answer