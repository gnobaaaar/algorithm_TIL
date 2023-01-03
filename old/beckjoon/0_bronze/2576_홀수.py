min = 1000
total = 0

for i in range(7):x
    num = int(input())
    if num % 2 == 1:
        total += num
        if num < min:
            min = num

if total == 0:
    print('-1')
else:
    print(total)
    print(min)