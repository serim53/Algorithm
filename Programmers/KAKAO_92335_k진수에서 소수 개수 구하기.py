import math

def change(n, k):
    num = ""
    while n:
        num = str(n % k) + num
        n = n // k
    return num

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_number = change(n, k)
    k_number = k_number.split("0")
    for n in k_number:
        if n == '':
            continue
        if is_prime_number(int(n)):
            answer += 1
    return answer


print(solution(110011, 10))