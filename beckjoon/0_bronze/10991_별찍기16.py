num = int(input())
for i in range(1, num+1):
    if i == num:
        print(('*'+' ')*i)
    else:
        print(' '*(num-i), end='')
        print(('*'+' ')*i)