import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    max_index = 0
    max_h = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        if max_h < mountain_h:
            max_h = mountain_h
            max_index = i
    print(max_index)

    # The index of the mountain to fire on.
