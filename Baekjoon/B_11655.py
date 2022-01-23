s = input()
result = ''
for c in s:
    if 'a' <= c <= 'z':
        result += chr((ord(c) + 13) if c <= 'm' else ord(c) - 13)
    elif 'A' <= c <= 'Z':
        result += chr((ord(c) + 13) if c <= 'M' else ord(c) - 13)
    else:
        result += c
print(result)