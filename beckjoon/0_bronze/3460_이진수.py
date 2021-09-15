len = int(input())

for i in range(len):
    n = int(input())
    count = 0
    while n > 0:
        if n == 1:
            print(count, end=" ")
            break

        elif n % 2 == 1:
            print(count, end=" ")
            count += 1
            n = n // 2

        else:
            n = n // 2
            count += 1
    print()

