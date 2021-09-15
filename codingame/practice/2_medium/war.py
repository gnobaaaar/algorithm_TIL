import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of cards for player 1
# for i in range(n):
#     cardp_1 = input()  # the n cards of player 1
# n_list = [input() for i in range(n)]
n_list = ['AD', 'KC', 'QC']

m = int(input())  # the number of cards for player 2
# for i in range(m):
#     cardp_2 = input()  # the m cards of player 2
# m_list = [input() for j in range(m)]
m_list = ['KH', 'QS', 'JC']

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def get_rank(words):
    if words[:-1] == 'J':
        return 11
    elif words[:-1] == 'Q':
        return 12
    elif words[:-1] == 'K':
        return 13
    elif words[:-1] == 'A':
        return 14
    else:
        return int(words[:-1])

