# 1월 1일은 월요일
# 1, 3, 5, 7, 8, 10, 12 => 31일
# 4, 6, 9, 11 => 30일
# 2월 => 28일

n, m = map(int, input().split())
total = 0
for i in range(1, n):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        total += 31
    elif i == 4 or i == 6 or i == 9 or i == 11:
        total += 30
    else:
        total += 28

total += m

total = total % 7


if total == 1:
    print("MON")
elif total == 2:
    print("TUE")
elif total == 3:
    print("WED")
elif total == 4:
    print("THU")
elif total == 5:
    print("FRI")
elif total == 6:
    print("SAT")
else:
    print("SUN")
