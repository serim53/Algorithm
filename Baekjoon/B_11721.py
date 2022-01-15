inputStr = input()
count = 0


while len(inputStr) - count >= 10:
    print(inputStr[count:count + 10])
    count += 10

print(inputStr[count:])
