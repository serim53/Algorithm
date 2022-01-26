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
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in range(M):
    if binary_search(cards, check[i], 0, N - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
