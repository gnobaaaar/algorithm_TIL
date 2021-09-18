x = int(input())
y = int(input())

if x > 0 and y >0:
    print(1)
elif x < 0 and y >0:
    print(2)
elif x < 0 and y <0:
    print(3)
else:
    print(4)

    # a = int(input())
    # b = int(input())
    # if a > 0:
    #     print(1 if b > 0 else 4)
    # elif a < 0:
    #     print(2 if b > 0 else 3)