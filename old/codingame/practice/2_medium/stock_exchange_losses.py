import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
max_target = 0
max_loss = 0
for i in input().split():
    if max_target < int(i):
        max_target = int(i)
    else:
        if max_loss > int(i) - max_target:
            max_loss = int(i) - max_target


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(max_loss)