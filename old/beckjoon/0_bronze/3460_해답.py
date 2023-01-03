# for _ in range(int(input())):
#     n = int(input())
#     i = 0
#     while n > 0:
#         if n%2 == 1:
#             print(i, end=' ')
#         n = n//2
#         i += 1

# bin -> 십진수를 2진수로 변환

for _ in range(int(input())):
    n = int(input())
    b = bin(n)[2:]
    for i in range(len(b)):
        if b[::-1][i] == '1':
            print(i, end=' ')