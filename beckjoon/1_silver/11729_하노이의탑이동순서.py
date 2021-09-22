def hanoi(n, from_pos, to_pos, tmp_pos):
    if n == 1:
        print(from_pos, to_pos)

    else:
        hanoi(n-1, from_pos, tmp_pos, to_pos)
        print(from_pos, to_pos)
        hanoi(n-1, tmp_pos, to_pos, from_pos)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)