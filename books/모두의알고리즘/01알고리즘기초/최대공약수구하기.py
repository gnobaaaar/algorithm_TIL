def gcd(a, b):
    tmp = 0
    if a < b:
        tmp = a
    else:
        tmp = b

    while tmp != 1:
        if a % tmp == 0 and b % tmp == 0:
            return tmp
        else:
            tmp -= 1

    return tmp


print(gcd(1, 5))    # 1
print(gcd(3, 6))    # 3
print(gcd(60, 24))  # 12
print(gcd(81, 27))  # 27