for i in range(int(input())):
    stack = []
    user_str = list(map(str, input()))
    for j in user_str:
        if j == '(':
            stack.append(j)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(j)
    if stack:
        print('NO')
    else:
        print('YES')