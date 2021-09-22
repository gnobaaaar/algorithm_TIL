def return_hansu(num):
    total = 0
    for i in range(1, num+1):
        if i < 100:
            total += 1
        else:
            a = list(str(i))
            if int(a[2]) - int(a[1]) == int(a[1]) - int(a[0]):
                total += 1
    return total

a = int(input())
print(return_hansu(a))