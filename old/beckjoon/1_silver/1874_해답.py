n = int(input())

stack = []
output = []
count = 1   # 스택의 빈 공간 확인

for i in range(1, n+1):
    data = int(input())     # 4 3 6 8 ...
    while count <= data:
        stack.append(count)
        count += 1
        output.append('+')

    if stack[-1] == data:
        stack.pop()
        output.append('-')
    else:
        print('NO')
        exit(0)

# possible
print('\n'.join(output))


