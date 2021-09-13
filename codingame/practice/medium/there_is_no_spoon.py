import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

a = [[0 for j in range(width)] for i in range(height)]

for i in range(height):
    line = input()  # width characters, each either 0 or .
    for j in range(width):
        a[i][j] = line[j]


def find_bottom(height, width, i, j, a):
    for y in range(i + 1, height):
        if a[y][j] == '0':
            return (j, y)
    return (-1, -1)


def find_right(height, width, i, j, a):
    for x in range(j + 1, width):
        if a[i][x] == '0':
            return (x, i)
    return (-1, -1)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for i in range(height):
    for j in range(width):
        if a[i][j] == '0':
            print("{0} {1} ".format(j, i), end='')

            b_x, b_y = find_right(height, width, i, j, a)
            print("{0} {1} ".format(b_x, b_y), end='')

            r_x, r_y = find_bottom(height, width, i, j, a)
            print("{0} {1} ".format(r_x, r_y))

# Three coordinates: a node, its right neighbor, its bottom neighbor

