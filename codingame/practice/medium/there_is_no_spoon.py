import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

# 2차원 배열의 생성
# a = []    # 빈 리스트 생성
#
# for i in range(3):
#     line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
#     for j in range(2):
#         line.append(0)     # 안쪽 리스트에 0 추가
#     a.append(line)         # 전체 리스트에 안쪽 리스트를 추가

a = [[0 for j in range(width)] for i in range(height)]
for i in range(height):
    line = input()  # width characters, each either 0 or .
    for j in range(width):
        a[i][j] = line[j]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in range(height):
    for j in range(width):
        if a[i][j] == '0':
            print('0 0 ', end='')

        if j+1 < width and a[i][j+1] == '0':
            print('0 0 ', end='')
        else:
            print('-1 -1 ', end='')

        if i+1 < height and a[i+1][j] == '0':
            print('0 0 ', end='')
        else:
            print('-1 -1 ', end='')
        print()


# Three coordinates: a node, its right neighbor, its bottom neighbor

