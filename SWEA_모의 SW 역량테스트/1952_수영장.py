t = int(input())
for tc in range(1, t + 1):
    day, month, three_month, year = map(int, input().split())
    plans = list(map(int, input().split()))
    expense = [0 for _ in range(12)]
    for i in range(12):
        expense[i] = min(plans[i] * day, month) + expense[i - 1]
        if i > 1:
            expense[i] = min(expense[i], three_month + expense[i - 3])
    result = min(expense[11], year)
    print("#{} {}".format(tc, result))