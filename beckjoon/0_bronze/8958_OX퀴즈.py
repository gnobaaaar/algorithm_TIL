def make_sum(array):
    sum = 0
    total = 0
    for i in array:
        if i == 'O':
            sum += 1
            total += sum
        if i == 'X':
            sum = 0
            total += sum
    return total

T = int(input())
for i in range(T):
    total = make_sum(list(map(str, input())))
    print(total)