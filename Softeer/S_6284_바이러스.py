k, p, n = map(int, input().split())
result = k
for _ in range(n):
    # 곱셈 연산은 수의 길이에 시간 복잡도가 비례한다.
    # 매 연산마다 수의 길이를 나눠주어 시간을 줄이도록 한다.
    result = result * p
    result = result % 1000000007
print(result % 1000000007)
