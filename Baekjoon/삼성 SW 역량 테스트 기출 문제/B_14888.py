import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

maximum = -1e9
minimum = 1e9


def dfs(cnt, result, plus, minus, multiply, divide):
    global maximum, minimum
    if cnt == n:
        maximum = max(result, maximum)
        minimum = min(result, minimum)
        return

    if plus:
        dfs(cnt + 1, result + nums[cnt], plus - 1, minus, multiply, divide)
    if minus:
        dfs(cnt + 1, result - nums[cnt], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(cnt + 1, result * nums[cnt], plus, minus, multiply - 1, divide)
    if divide:
        dfs(cnt + 1, int(result / nums[cnt]), plus, minus, multiply, divide - 1)


dfs(1, nums[0], operator[0], operator[1], operator[2], operator[3])

print(maximum)
print(minimum)
