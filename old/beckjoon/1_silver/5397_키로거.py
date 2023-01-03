# 다시 생각하기
import sys

for _ in range(int(input())):
    left, right = [], []
    user_list = list(sys.stdin.readline().rstrip())

    for i in user_list:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    while right:
        left.append(right.pop())
    print(''.join(left))