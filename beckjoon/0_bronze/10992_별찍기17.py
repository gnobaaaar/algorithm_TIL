num = int(input())
for i in range(1, num+1):
    if i == num:
        print(('*')*(2*i-1))
    elif i ==1:

        print(' '*(num-i), end='')
        print('*', end='')
    else:
        print(' '*(num-i), end='')
        print('*', end='')
        print(' '*(2*(i-1)-1),end='')
        print('*', end='')
    print()