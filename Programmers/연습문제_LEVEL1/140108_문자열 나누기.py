def solution(s):
    answer = 0
    temp = s[0]
    same, diff = 1, 0
    for i in range(1, len(s)):
        if temp == s[i]:
            same += 1
        else:
            diff += 1
        if same == diff:
            answer += 1
            if i + 1 < len(s):
                temp, same, diff = s[i + 1], 0, 0
            else:
                temp, same, diff = "", 0, 0
    if same != 0 or diff != 0 or temp != "":
        answer += 1
    return answer
