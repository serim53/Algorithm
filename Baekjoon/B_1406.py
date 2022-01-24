import sys
st_left = list(sys.stdin.readline().rstrip())
st_right = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if st_left:
            st_right.append(st_left.pop())
    elif command[0] == 'D':
        if st_right:
            st_left.append(st_right.pop())
    elif command[0] == 'B':
        if st_left:
            st_left.pop()
    else:
        st_left.append(command[1])

st_left.extend(reversed(st_right))
print(''.join(st_left))
