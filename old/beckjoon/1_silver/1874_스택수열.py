stack = []
output = []
tmp = 0
result = ''

for i in range(int(input())):
    num = int(input())
    if len(stack) == 0 or stack[-1] < num:
        for j in range(tmp+1, num+1):
            stack.append(j)
            output.append('+')
        stack.pop()
        output.append('-')
        tmp = num
    elif stack[-1] == num:
        stack.pop()
        output.append('-')
    else:
        result = 'NO'

if result == 'NO':
    print(result)
else:
    for i in output:
        print(i)