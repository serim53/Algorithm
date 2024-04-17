def find_bingo(str):
    # 가로
    for i in range(0, 9, 3):
        if input_str[i] == str and input_str[i] == input_str[i + 1] == input_str[i + 2]:
            return True

    # 세로
    for i in range(3):
        if str == input_str[i] and input_str[i] == input_str[i + 3] == input_str[i + 6]:
            return True

    # 대각선
    if str == input_str[0] and input_str[0] == input_str[4] == input_str[8]:
        return True

    if str == input_str[2] and input_str[2] == input_str[4] == input_str[6]:
        return True

    return False

while True:
    input_str = str(input().rstrip())
    if input_str == 'end':
        break
    bingo_o, bingo_x = find_bingo('O'), find_bingo('X')
    num_o, num_x = input_str.count('O'), input_str.count('X')
    if bingo_x and not bingo_o and num_x == num_o + 1:
        print("valid")
        continue
    if bingo_o and not bingo_x and num_o == num_x:
        print("valid")
        continue
    if not bingo_o and not bingo_x and num_x == 5 and num_o == 4:
        print("valid")
        continue
    print("invalid")