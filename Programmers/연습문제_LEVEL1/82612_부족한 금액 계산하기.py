def solution(price, money, count):
    need_price = price * (count * (count + 1) // 2)
    return max(0, need_price - money)