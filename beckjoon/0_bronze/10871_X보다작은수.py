import sys

n, x = map(int, sys.stdin.readline().split())

for i in sys.stdin.readline().split():
    if int(i) < x:
        print(i, end=" ")