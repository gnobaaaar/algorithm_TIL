import sys

T = int(input())

for i in range(T):
    total = 0
    index = 0
    array = list(map(int, sys.stdin.readline().split()))
    for j in range(1, array[0]+1):
        total += array[j]
    avg = total / array[0]
    for j in range(1, array[0] + 1):
        if array[j] > avg:
            index += 1
    num = index / array[0]
    print('{:.3f}%'.format(round(num*100, 3)))