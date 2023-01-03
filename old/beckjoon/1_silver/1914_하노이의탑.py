def hanoi(n, from_pos, to_pos, tmp_pos):
    if n == 1:
        print(from_pos, to_pos, sep=" ")
        return
    hanoi(n-1, from_pos, tmp_pos, to_pos)
    print(from_pos, to_pos, sep=" ")
    hanoi(n-1, tmp_pos, to_pos, from_pos)

num = int(input())
print(2**num-1)
if num <= 20:
    hanoi(num, 1, 3, 2)