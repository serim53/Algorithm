decode = {
    '112' : 0, '122':1, '221':2,'114':3, '231':4,'132':5, '411':6, '213':7, '312':8, '211':9}
hex_to_bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}


def examine(arr): #검증조건 맞는지
    if ((arr[7]+arr[5]+arr[3]+arr[1])*3 + arr[0]+arr[2]+arr[4]+arr[6]) % 10:
        return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    big_code = [input()[:m] for _ in range(n)]
    visited = []
    ans = 0
    for i in range(n):
        binarified = ''
        for char in big_code[i]:
            binarified += hex_to_bin[char]
        big_code[i] = binarified
    res = []
    for i in range(n):
        f1 = f2 = f3 = 0
        if '1' not in big_code[i]:
            continue
        for m in range(m * 4 - 1, -1, -1):
            if f2 == 0 and f3 == 0 and big_code[i][m] == '1': #첫 1
                f1 += 1
            elif f1 and f3 == 0 and big_code[i][m] == '0': #10
                f2 += 1
            elif f1 and f2 and big_code[i][m] == '1': #101
                f3 += 1
            elif f3 and big_code[i][m] == '0':
                mul = min(f1, f2, f3)
                res.append(decode[str(f1//mul)+str(f2//mul)+str(f3//mul)])
                f1 = f2 = f3 = 0
                if len(res) == 8:
                    if res not in visited:
                        if examine(res):
                            ans += sum(res)
                        visited.append(res)
                    res = []
    print('#{} {}'.format(test_case, ans))