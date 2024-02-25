n = int(input())
words = []
for _ in range(n):
     words.append(input().rstrip())
dict = {}
for word in words:
    digit = len(word) - 1
    for i in word:
        if i in dict:
            dict[i] += 10 ** digit
        else:
            dict[i] = 10 ** digit
        digit -= 1

values = sorted(dict.values(), reverse=True)
result = 0
num = 9
for v in values:
    result += v * num
    num -= 1
print(result)