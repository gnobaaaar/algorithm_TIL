import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n==0:
    print('0')
else:
    min_t = 5527
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
        if abs(t) < abs(min_t):
            min_t = t
        elif abs(t) == abs(min_t):
            if t > 0:
                min_t = t
    print(min_t)


