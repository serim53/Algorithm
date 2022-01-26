import sys

# 가지고 있는 카드 개수
N = int(sys.stdin.readline())
# 가지고 있는 카드 숫자
cards = list(map(int, sys.stdin.readline().split()))
# 검사해야 할 카드 개수
M = int(sys.stdin.readline())
# 검사해야 할 카드 숫자
check = list(map(int, sys.stdin.readline().split()))

cards.sort()

def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result += 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return result


for i in range(M):
    print(str(binary_search(cards, check[i], 0, N - 1)), end=' ')
