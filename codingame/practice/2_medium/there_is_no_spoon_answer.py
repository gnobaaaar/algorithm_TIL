import sys
import math

width = int(input())
height = int(input())


def parse_lines():
    lines = []
    for i in range(height):
        line = input()
        lines.append(list(line))
    return lines


def node_exists(nx, ny):
    return nx < width and ny < height and lines[ny][nx] == "0"


def find_right_neighbour(x, y):
    for i in range(width - x):
        rx, ry = x + 1 + i, y

        if node_exists(rx, ry):
            return (rx, ry)
    return (-1, -1)


def find_down_neighbour(x, y):
    for i in range(height - y):
        dx, dy = x, y + 1 + i

        if node_exists(dx, dy):
            return (dx, dy)
    return (-1, -1)


lines = parse_lines()

for y in range(height):
    for x in range(width):
        c = lines[y][x]
        if c == ".":
            continue

        rightNode = find_right_neighbour(x, y)
        downNode = find_down_neighbour(x, y)

        coordinates = "{0} {1} {2} {3} {4} {5}".format(x, y, rightNode[0], rightNode[1], downNode[0], downNode[1])
        print(coordinates)