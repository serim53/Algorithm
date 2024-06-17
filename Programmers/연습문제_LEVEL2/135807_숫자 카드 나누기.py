import math

answer = 0

def get_gdc(arr):
    a = arr[0]
    for b in arr[1:]:
        a = math.gcd(a, b)
    return a

def check(num, arr):
    global answer
    for b in arr:
        if b % num == 0:
            break
    else:
        answer = max(num, answer)

def solution(arrayA, arrayB):
    a_gdc, b_gdc = get_gdc(arrayA), get_gdc(arrayB)
    check(a_gdc, arrayB)
    check(b_gdc, arrayA)
    return answer