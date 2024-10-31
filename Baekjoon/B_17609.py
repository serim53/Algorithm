# 회문이면 0, 유사회문이면 1, 그 외는 2
def check(input_str):
    start, end = 0, len(input_str) - 1
    while start <= end:
        if input_str[start] == input_str[end]:
            start += 1
            end -= 1
        else:
            if start + 1 == end:
                return 1
            if start < end - 1:
                temp = input_str[:end] + input_str[end + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            if start + 1 < end:
                temp = input_str[:start] + input_str[start + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0
t = int(input())
for _ in range(t):
    print(check(list(input())))
