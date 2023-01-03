import math

def solution(n):
    tmp = int(math.sqrt(n))

    if math.pow(tmp, 2) == n:
        return math.pow(tmp + 1, 2)
    else:
        return -1