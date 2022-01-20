n = int(input())
array = []
for i in range(n):
    name, korean, english, math = map(str, input().split())
    korean = int(korean)
    english = int(english)
    math = int(math)
    array.append((name, korean, english, math))

array.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in array:
    print(i[0])