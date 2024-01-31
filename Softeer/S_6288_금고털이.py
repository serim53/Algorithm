import sys
input = sys.stdin.readline

w, n = map(int, input().split())
sum_weight = 0
price = 0
metals = []
for _ in range(n):
    m, p = map(int, input().split())
    metals.append([m, p])
metals.sort(key=lambda x: -x[1])
idx = -1
while idx <= n - 2:
    idx += 1
    if sum_weight + metals[idx][0] > w:
        break
    sum_weight += metals[idx][0]
    price += metals[idx][1] * metals[idx][0]

price += (w - sum_weight) * metals[idx][1]
print(price)