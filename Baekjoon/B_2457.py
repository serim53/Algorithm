n = int(input())
flowers = []
for _ in range(n):
    start_m, start_d, end_m, end_d = map(int, input().split())
    flowers.append([start_m * 100 + start_d, end_m * 100 + end_d])
flowers.sort()

end_date = 301
result = 0

while flowers:
    if end_date >= 1201 or flowers[0][0] > end_date:
        break

    temp_end_date = -1

    for _ in range(len(flowers)):
        if flowers[0][0] <= end_date:
            if temp_end_date <= flowers[0][1]:
                temp_end_date = flowers[0][1]
            flowers.pop(0)
        else:
            break

    end_date = temp_end_date
    result += 1

print(result if end_date >= 1201 else 0)