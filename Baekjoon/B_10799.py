inp = list(input())
result = 0
st = []

for i in range(len(inp)):
    if inp[i] == '(':
        st.append('(')

    else:
        if inp[i - 1] == '(':
            st.pop()
            result += len(st)

        else:
            st.pop()
            result += 1

print(result)